# app.py
from flask import Flask, jsonify  #import modules
from newsfeed import getWaPo
app = Flask(__name__) #instatiate class


app = Flask(__name__)

@app.route('/')  #decorator defines the URI
def index():
    return jsonify(Products=getWaPo())
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)


#change the data to JSON