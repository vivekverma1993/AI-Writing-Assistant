import os

# Create necessary directories if they don't exist
os.makedirs('app/services', exist_ok=True)

# main.py
with open('main.py', 'w') as f:
    f.write('''from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
''')

# app/__init__.py
with open('app/__init__.py', 'w') as f:
    f.write('''from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
''')

# app/routes.py
with open('app/routes.py', 'w') as f:
    f.write('''from flask import Blueprint, request, jsonify
from .services.generate import generate_text
from .services.grammar_check import check_grammar
from .services.summarization import summarize_text

main_bp = Blueprint('main', __name__)

@main_bp.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        generated_text = generate_text(prompt)
        return jsonify({'generated_text': generated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/check_grammar', methods=['POST'])
def check():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        grammar_result = check_grammar(text)
        return jsonify({'grammar_result': grammar_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        summary = summarize_text(text)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
''')

# app/services/generate.py
with open('app/services/generate.py', 'w') as f:
    f.write('''import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_text(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['text'].strip()
''')

# app/services/grammar_check.py
with open('app/services/grammar_check.py', 'w') as f:
    f.write('''# Placeholder for grammar check logic using external API or custom model

def check_grammar(text):
    # Implement grammar checking logic
    return "Grammar check completed (mock response)"
''')

# app/services/summarization.py
with open('app/services/summarization.py', 'w') as f:
    f.write('''# Placeholder for summarization logic using LLMs

def summarize_text(text):
    # Implement text summarization logic
    return "Summary of the text (mock response)"
''')

# .env
with open('.env', 'w') as f:
    f.write('''OPENAI_API_KEY=your_openai_api_key_here
''')

# requirements.txt
with open('requirements.txt', 'w') as f:
    f.write('''openai
flask
python-dotenv
''')
