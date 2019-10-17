from flask import render_template
from app import app #import app variable, which is a member of the app package
from app.forms import LoginForm
from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2
from datetime import date


source = requests.get('https://www.washingtonpost.com/').text
soup = BeautifulSoup(source, 'lxml')

front_page = soup.find("section", {"id": "main-content"})
articles = front_page.findAll(True, {'class':['headline x-small normal-style text-align-inherit', 'headline small normal-style text-align-inherit', 'headline xx-small normal-style text-align-inherit']})
                                                                                                                  


@app.route('/')
def index():
    today = date.today()
    today_str = today.strftime("%A, %b %d")
    print(today_str)

    count = 0 
    waPo_articles = []
    for article in articles:
        a = { }
        if article.find('a') is None:
            continue
        elif count <10:
            count += 1    
            print(count)
            link = article.find('a')
            summary = article.find_next_sibling("div")
            a['link_text'] = link.text
            a['link_url'] = link['href']
            if summary:
                a['link_summary'] = summary.text
            else:
                a['link_summary'] = 'No summary given'
            waPo_articles.append(a)
        else: 
            break
        
        
    return render_template('index.html', waPo_articles= waPo_articles, today_str= today_str)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
