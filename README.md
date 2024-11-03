# Project: Large Language Model (LLM) Interface in Python

## Overview
This project is a Python-based interface designed to interact with a large language model (LLM). The goal is to build a modular and scalable system that processes user input, generates model predictions, and outputs responses through a robust, multi-file architecture.

## Features
- **Text Generation**: Generate creative and informative text based on user prompts.
- **Grammar Checking**: Analyze and correct grammar in input text.
- **Text Summarization**: Summarize long pieces of text efficiently.

## Project Structure
```
project-folder/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── generate.py
│   │   ├── grammar_check.py
│   │   └── summarization.py
├── .env
├── main.py
└── requirements.txt
```

## Getting Started

### Prerequisites
Ensure you have Python 3.x installed and the following packages:
- `openai`
- `flask`
- `python-dotenv`

Install them with:
```bash
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Running the Application
1. **Navigate to the project folder**:
   ```bash
   cd project-folder
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

The app will run locally on `http://127.0.0.1:5000`.

## API Endpoints

### 1. **Text Generation**
**Endpoint**: `/generate`  
**Method**: `POST`  
**Payload**:
```json
{
  "prompt": "Write a short story about AI."
}
```
**Response**:
```json
{
  "generated_text": "Once upon a time, an AI learned to write stories..."
}
```

### 2. **Grammar Checking**
**Endpoint**: `/check_grammar`  
**Method**: `POST`  
**Payload**:
```json
{
  "text": "This is a example sentence"
}
```
**Response**:
```json
{
  "grammar_result": "Grammar check completed (mock response)"
}
```

### 3. **Text Summarization**
**Endpoint**: `/summarize`  
**Method**: `POST`  
**Payload**:
```json
{
  "text": "Long text that needs summarization..."
}
```
**Response**:
```json
{
  "summary": "Summary of the text (mock response)"
}
```

## File Descriptions
- **`main.py`**: Entry point for running the Flask application.
- **`app/__init__.py`**: Initializes the Flask app and registers routes.
- **`app/routes.py`**: Defines the routes and request handling logic.
- **`app/services/generate.py`**: Handles text generation logic using OpenAI's API.
- **`app/services/grammar_check.py`**: Placeholder logic for grammar checking.
- **`app/services/summarization.py`**: Placeholder logic for text summarization.
- **`.env`**: Stores environment variables securely.
- **`requirements.txt`**: Lists required Python packages.

## Future Enhancements
- Integrate more robust grammar checking using third-party APIs.
- Enhance the summarization logic for more accurate results.
- Add more endpoints for various NLP tasks.

## Contributing
Feel free to fork this project, submit pull requests, or report issues.

## License
This project is licensed under the MIT License.

---
**Developed by Vivek Verma**
