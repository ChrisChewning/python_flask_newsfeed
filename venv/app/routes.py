from flask import render_template
from app import app #import app variable, which is a member of the app package
from newsfeed import getWaPo
from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2


@app.route('/')
def index():
    return jsonify(Products=getWaPo())

    # return render_template('index.html', title="Home")

    #     return jsonify(Products=getWaPo())



@app.route('/login')
def login():
    return render_template('index.html', title='Login')


#this grabs the summary without the extra information:

# headline_text = front_page.findAll(class_='blurb normal normal-style', limit=10)
    # for h in headline_text:
#     print(h.text)

