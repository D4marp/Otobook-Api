from flask import Flask, request, jsonify
from camera import capture_image
from ocr import extract_text
from gpt3 import get_summary
import joblib

app = Flask(__name__)

# Load the classifier model
model = joblib.load('model/book_classifier.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        image_path = capture_image()
        text = extract_text(image_path)
        return jsonify({'status': 'success', 'image_path': image_path, 'text': text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/extract', methods=['POST'])
def extract():
    try:
        data = request.json
        text = data['text']
        # Classify the book text
        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)[0]
        metadata = {
            'title': 'Extracted Title',  # Replace with OCR text extraction
            'author': 'Extracted Author',  # Replace with OCR text extraction
            'synopsis': get_summary(text),
            'classification': prediction
        }
        return jsonify(metadata)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
