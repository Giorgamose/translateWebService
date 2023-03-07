from flask import Flask, jsonify, request
import html

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    input_text = request.json.get('text')
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'key': 'AIzaSyBri2ufYJVFh5r4EBfxkpTC3FNyaujZgEo',
        'target': 'en',
        'source': 'ka',
        'q': input_text
    }
    response = requests.get(url, params=params).json()
    translated_text = response['data']['translations'][0]['translatedText']
    updated_text = html.unescape(translated_text)
    return jsonify({'result': updated_text})

if __name__ == '__main__':
    app.run(debug=True)

