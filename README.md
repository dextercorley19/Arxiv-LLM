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
git clone <your-repo-url>
cd arxiv-llm-app
