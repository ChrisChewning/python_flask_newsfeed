from flask import render_template
from app import app #import app variable, which is a member of the app package
from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2


source = requests.get('https://www.washingtonpost.com/').text
#lxml is the markup
soup = BeautifulSoup(source, 'lxml')

front_page = soup.find("section", {"id": "main-content"})
articles = front_page.findAll(True, {'class':['no-skin flex-item flex-stack normal-air text-align-left wrap-text equalize-height-target', 'no-skin flex-item flex-stack normal-air text-align-left equalize-height-target']}, limit=10)


@app.route('/')
def index():
    username= 'Chris'
    l = []
    for article in articles:
        a = { }
        if article.find('a') is None:
            continue
        else:
            link = article.find('a')
            print('article.find(a)', link)
            a['link_text'] = link.text
            a['link_url'] = link['href']
            if article.find(class_="blurb normal normal-style"):
                a['link_summary'] = article.text
            else:
                a['link_summary'] = 'No summary given'
            l.append(a)

    return render_template('index.html', l=l, username=username)


@app.route('/login')
def login():
    return render_template('index.html', title='Login')

        # a['link_text'] = link.text
        # a['link_url'] = link['href']

        #  if link.text:
        #         a['link_text'] = link.text
        #     a['link_url'] = link['href']
        # else: 
        #     continue