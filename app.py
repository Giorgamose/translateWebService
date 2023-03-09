import requests
import html
from flask import Flask, jsonify, request

app = Flask(__name__)
url = 'https://translation.googleapis.com/language/translate/v2'

@app.route('/translate', methods=['POST'])
def translate_text():
    input_text = request.json.get('text', '')
    target = request.json.get('target', '')
    source = request.json.get('source', '')
    if not input_text:
        return jsonify({'error': 'No input text provided.'})
    params = {
        'key': 'GoogleAppID',
        'target': target ,
        'source': source ,
        'q': input_text
    }
    response = requests.post(url, params=params).json()
    translated_text = response['data']['translations'][0]['translatedText']
    updated_text = html.unescape(translated_text)
    return jsonify({'result': updated_text})

if __name__ == '__main__':
    app.run(debug=True)
