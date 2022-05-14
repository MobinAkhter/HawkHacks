#Authentication header
# curl --request GET \
#   --url https://api.assemblyai.com/v2/ \
#   --header 'authorization: YOUR-API-TOKEN'
"""Imports"""
# from bs4 import BeautifulSoup
# import requests
from distutils.log import debug
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

auth_key = 'a30b0d235ea04ce5946b07f391afd504'

@app.route('/', methods = ['POST', 'GET'])
def get_transcript():
    return render_template('index.html')
    
@app.route('/text', methods = ['GET', 'POST'])
def get_text():
    return render_template('text.html')

### Run App
app.run(debug=True)