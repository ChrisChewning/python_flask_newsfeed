from flask import Flask, render_template
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2


source = requests.get('https://www.washingtonpost.com/').text
#lxml is the markup
soup = BeautifulSoup(source, 'lxml')

front_page = soup.find("section", {"id": "main-content"})
headlines = front_page.findAll(class_='headline', limit=1)
summaries = front_page.findAll(class_='no-skin flex-item flex-stack normal-air text-align-left equalize-height-target', limit=1)         


from flask import Flask, render_template
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2


source = requests.get('https://www.washingtonpost.com/').text
soup = BeautifulSoup(source, 'lxml')

articles = front_page.findAll(class_='no-skin flex-item flex-stack normal-air text-align-left equalize-height-target', limit=10)         

for article in articles:
    link = article.find('a')
    print('link text: ', link.text)
    print('link: ', link['href'])
    print('summary: ', article.text)

