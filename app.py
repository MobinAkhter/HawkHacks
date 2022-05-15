#Authentication header
# curl --request GET \
#   --url https://api.assemblyai.com/v2/ \
#   --header 'authorization: YOUR-API-TOKEN'
"""Imports"""
# from bs4 import BeautifulSoup
# import requests
from distutils.log import debug
from flask import Flask, render_template, request, jsonify
from transcribe import transcribe_from_link

# Flask constructor
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home_page():
    return render_template('index.html')
    
@app.route('/transcribe', methods = ['GET', 'POST'])
def transcribe():
    if request.method == "POST":
        print("here1")
        url = request.form['videoURL']
        print("here2")
        polling_endpoint = transcribe_from_link(url,False)
        return render_template('success.html')
    return render_template('text.html')

### Run App
if __name__=='__main__':
   app.run(debug=True)