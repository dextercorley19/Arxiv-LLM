from fastapi import FastAPI
from pydantic import BaseModel
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import openai
import os
from selenium.webdriver.chrome.service import Service

app = FastAPI()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY") 

# Function to get embedding for a given text string (chunk)
def get_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    embedding = response['data'][0]['embedding']
    return embedding


# MongoDB client setup
client = MongoClient('mongodb://mongo:27017/') 
db = client['your_database']
text_collection = db['papers_text']
embedding_collection = db['embeddings']

# Pydantic model for URL input
class URLInput(BaseModel):
    url: str

class QuestionInput(BaseModel):
    question: str


def process_arxiv_url(url):
    #selenium navigating to html version of paper
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.get(url)
    to_html_xpath = '//*[@id="latexml-download-link"]'
    button = driver.find_element(By.XPATH, to_html_xpath)
    button.click()
    #get soup
    soup = BeautifulSoup(driver.page_source, 'html.parser')    
    
    # get content (chunks) of the paper, each subsection representing a chunk of text
    # abstract section
    abstract = soup.find('h6')
    for x in abstract.find_next_siblings():
        abstract_text = ''
        abstract_text += x.text
    chunks = {abstract.text:abstract_text}
        
    # all other sections
    h2_tags = soup.find_all('h2')
    topics = {}
    for i,h in enumerate(h2_tags):
        text = h.text
        if len(text.split()) > 1:
            topics[text.split()[1]] = ''
        else:
            break
        for sibling in h2_tags[i].find_next_siblings():
            topics[text.split()[1]] += sibling.text
    chunks.update(topics)
    
    #get embeddings for each chunk
    for title,chunk in chunks.items():
        if chunk.strip():  # Check if chunk is not empty
            # Save text chunk to MongoDB
            text_collection.insert_one({"title": title, "text": chunk})

            # Get embedding for the text chunk
            embedding = get_embedding(chunk)  
            embedding_collection.insert_one({"title": title, "chunk": chunk, "embedding": embedding})
    driver.quit()


@app.post("/process-url")
def process_url(data: URLInput):
    process_arxiv_url(data.url)
    return {"message": "Processing complete, please navigate to 'Ask a Question' page!"}

@app.post("/ask-question")
def ask_question(data: QuestionInput):
    # Get embedding for the question
    question_embedding = get_embedding(data.question)

    # Retrieve all embeddings from MongoDB
    all_embeddings = list(embedding_collection.find({}))
    similarities = []

    # Calculate cosine similarity between the question embedding and stored embeddings
    for emb in all_embeddings:
        similarity = np.dot(question_embedding, emb['embedding'])
        similarities.append((emb['title'], emb['chunk'], similarity))

    # Sort by similarity and get the top 5 chunks
    print(similarities[2])
    top_answers = sorted(similarities, key=lambda x: x[2], reverse=True)[:5]
    print(top_answers)
    # Prepare context for ChatGPT API by concatenating top chunks
    context = " ".join([chunk for _, chunk, _ in top_answers])

    # Call the OpenAI ChatCompletion API to generate an answer
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
        messages=[
            {"role": "assistant", "content": f"Context: {context}\n\nQuestion: {data.question}"}
        ],
        max_tokens=1000,  # You can adjust this limit based on your needs
        temperature=0.7  # Control randomness; adjust for more creative responses
    )

    # Extract the answer from the API response
    answer = response.choices[0].message['content']

    return {"answer": answer}

