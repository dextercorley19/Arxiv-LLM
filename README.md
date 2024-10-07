# arXiv LLM App

Welcome to the **arXiv LLM App**! This application allows users to input an arXiv paper URL, processes the content, and retrieves valuable insights using OpenAI's gpt-3.5-turbo LLM. Built with a FastAPI backend and a Next.js frontend, this app provides an interactive way to explore research papers.


## Features

- Input an arXiv paper URL.
- Fetch and process the paper's text.
- Generate embeddings for efficient similarity searching.
- Utilize OpenAI's API to answer questions based on the paper's content.

## Technologies Used

- **Frontend**: Next.js, React, Tailwind CSS
- **Backend**: FastAPI, Python
- **Database**: MongoDB (Dockerized)
- **Deployment**: Docker

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

or 

- Docker & Docker Compose

## Setup Instructions

### 1. Clone the Repository

```bash
cd path/to/destination/dir
git clone https://github.com/dextercorley19/arXiv-LLM
cd arxiv-llm-app
```

### 2. Pass in your OpenAI API key

Navigate to docker-compose.yml and pass in your api key where specified.

### 3. Build and Run the Application

Use Docker Compose to build and start the application. This command will set up both the frontend and backend services along with the MongoDB database. In /arxiv-llm-app run:

```bash
docker compose up --build
```

### 4. Access the Application

Open your web browser and navigate to http://localhost:3000. You will see the interface where you can input an arXiv paper URL. Once processed, the page will let you know to navigate to "Ask a question" where you can talk with ChatGPT about the paper.

### Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License.
