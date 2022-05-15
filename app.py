#Authentication header
# curl --request GET \
#   --url https://api.assemblyai.com/v2/ \
#   --header 'authorization: YOUR-API-TOKEN'
"""Imports"""
# from bs4 import BeautifulSoup
# import requests
from distutils.log import debug
from email import message
from flask import Flask, render_template, request, jsonify
from transcribe import transcribe_from_link, check_transcript_status


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
        global polling_endpoint
        polling_endpoint = transcribe_from_link(url,False)
        return render_template('video.html')
    # return render_template('index.html')

    if request.method == "GET":
        # message = {'trancript_id:' f'{transcript_id}'}
        # return jsonify(message)
        check_transcript_status(polling_endpoint)

### Run App
if __name__=='__main__':
   app.run(debug=True)