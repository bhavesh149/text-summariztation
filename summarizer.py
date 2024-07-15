import click
import requests
import sys
from dotenv import load_dotenv
import os

load_dotenv()

# OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL')

def summarize_text(text):
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
    
    payload = {
        "model": "qwen2:0.5b",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        summary = response.json()["response"].strip()
        return summary
    except requests.RequestException as e:
        print(f"Error: Unable to connect to Ollama API. {str(e)}")
        sys.exit(1)

@click.command()
@click.option('-t', '--text-file', type=click.Path(exists=True), help='Path to the text file for summarization')
@click.argument('text', required=False)
def main(text_file, text):
    if text_file:
        with open(text_file, 'r') as file:
            content = file.read()
        summary = summarize_text(content)
        print(f"Summary of {text_file}:")
    elif text:
        summary = summarize_text(text)
        print("Summary of text pasted:")
    else:
        print("Error: Please provide either a text file or direct text input.")
        sys.exit(1)
    
    print(summary)

if __name__ == '__main__':
    main()