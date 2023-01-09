from flask import Flask, redirect, url_for, render_template, request, jsonify
from decouple import config

import os
import uuid
import base64

BASE_URL = config('SERVER_URL')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', dr=BASE_URL)

@app.route('/data-buku')
def dataBuku():
    return render_template('data-buku.html', dr=BASE_URL)

@app.route('/data-kategori')
def dataKategori():
    return render_template('data-kategori.html', dr=BASE_URL)

# jalankan server 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7009)