from flask import Blueprint, request, jsonify
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
