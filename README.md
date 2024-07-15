# Text Summarization CLI

This command-line application uses the Ollama API to summarize text input or text from a file with Qwen2 0.5B model.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Ollama

## Setup

1. Clone the repository:
```
  git clone https://github.com/bhavesh149/text-summariztation.git
```
```
  cd text-summariztation
```

2. Create a virtual environment (optional but recommended):
```
  python -m venv venv
```
3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install the required packages:
```
  pip install -r requirements.txt
```
5. Update a `.env` file in the root directory and add the Ollama API URL(if needed):

Replace the URL with your Ollama API endpoint if different.

## Usage

Run the application using one of the following commands:

1. To summarize text from a file:
```
  python summarizer.py -t path/to/your/text/file.txt
```
2. To summarize text directly from the command line:
```
  python main.py "Your text to summarize goes here."
```

## Troubleshooting

If you encounter any issues:

1. Ensure that the Ollama API is running and accessible.
2. Check that the API URL in the `.env` file is correct.
3. Make sure all required packages are installed.