from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    translated_text = ''
    if request.method == 'POST':
        text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        url = "https://libretranslate.com/translate"


        payload = {
            'q': text,
            'source': source_lang,
            'target': target_lang,
            'format': 'text'
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)

            # Debug the status code and text
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)

            if response.status_code == 200:
                data = response.json()
                translated_text = data.get('translatedText', 'No translation found')
            else:
                translated_text = f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            translated_text = f"Request failed: {str(e)}"

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
