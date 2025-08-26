# Flipkart Product Recommendation System App

## Installation:
### Local/Virtual Environment:
Run `pip install -r requirements.txt`

### Docker:
A `Dockerfile` is included. Build the image via `docker build -t llmops-app:latest .` or using `docker-compose`

## AstraDB + Groq API Keys + Huggingface Hub User API Access Token:
It will be necessary to create an AstraDB database + API key, a Groq API key and a Huggingface Hub API token. These should be stored in a `.env` file in the project
root directory. An `env_dummy.txt` file is provided with the appropriate keys as a reference.
(N.b.: `HF_TOKEN` and `HUGGINGFACEHUB_API_TOKEN` should be identical.) <br />
AstraDB: https://astra.datastax.com/<br />
Groq: https://console.groq.com/keys <br /> 
Huggingface Hub: https://huggingface.co/settings/tokens

## Running the App:
From the project root directory, execute: `python app.py`


