from flask import Flask, request, jsonify
from app.emotion_detector import detect_emotion

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Text input is required'}), 400
    result = detect_emotion(data['text'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
