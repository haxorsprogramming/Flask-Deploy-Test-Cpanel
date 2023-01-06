from flask import Flask, redirect, url_for, render_template, request, jsonify

import os
import uuid
import base64

BASE_URL = os.getenv('SERVER_URL')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', dr=BASE_URL)

# jalankan server 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7009)