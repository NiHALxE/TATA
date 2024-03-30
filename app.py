import os
import base64
import time
from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

STREAMS = {
    'Hindi': 'https://api.nayeem-parvez.pw/jclive2/master.m3u8?id=hd_akamai_androidmob_avc_hin_ipl_s1_m3090324&uid=2100323',
    'Bangla': 'https://api.nayeem-parvez.pw/jclive/master.m3u8?id=hd_akamai_androidmob_avc_ben_ipl_s1_m1300324&uid=2109774',
    'English': 'https://api.nayeem-parvez.pw/jclive2/master.m3u8?id=hd_akamai_androidmob_avc_eng_ipl_s1_m1300324&uid=2100299'
}

temp_url_mappings = {}

@app.route('/')
def index():
    return render_template('index.html', streams=STREAMS.keys())

@app.route('/stream/<language>')
def stream(language):
    real_url = STREAMS.get(language)
    if real_url:
        temp_url = generate_temp_url(real_url)
        temp_url_mappings[temp_url] = real_url
        return temp_url
    else:
        return "Invalid Stream", 404

@app.route('/temp/<temp_url>')
def serve_stream(temp_url):
    real_url = temp_url_mappings.get(temp_url)
    if real_url:
        return send_from_directory('.', 'stream.m3u8', as_attachment=False)  
    else:
        return "Invalid Stream", 404

def generate_temp_url(real_url):
    encoded_url = base64.b64encode(real_url.encode()).decode()
    timestamp = str(int(time.time()))
    return f"stream_{encoded_url}_{timestamp}"  

if __name__ == "__main__":
    app.run()
