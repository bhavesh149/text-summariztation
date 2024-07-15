import click
import requests
import sys
import json
from dotenv import load_dotenv
import os

load_dotenv()
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL')

def summarize_text_stream(text):
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
   
    payload = {
        "model": "qwen2:0.5b",
        "prompt": prompt,
        "stream": True
    }
   
    try:
        with requests.post(OLLAMA_API_URL, json=payload, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line)
                        if 'response' in data:
                            yield data['response']
                    except json.JSONDecodeError:
                        continue
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
        print(f"Summary of {text_file}:")
    elif text:
        content = text
        print("Summary of text pasted:")
    else:
        print("Error: Please provide either a text file or direct text input.")
        sys.exit(1)
   
    print()  
    for text_chunk in summarize_text_stream(content):
        sys.stdout.write(text_chunk)
        sys.stdout.flush()
    print()  

if __name__ == '__main__':
    main()
    
    
