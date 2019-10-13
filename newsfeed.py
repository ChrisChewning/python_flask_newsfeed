from flask import Flask, render_template
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2


source = requests.get('https://www.washingtonpost.com/').text
#lxml is the markup
soup = BeautifulSoup(source, 'lxml')

front_page = soup.find("section", {"id": "main-content"})
headlines = front_page.findAll(class_='headline', limit=10)
summaries = front_page.findAll(class_='no-skin flex-item flex-stack normal-air text-align-left equalize-height-target', limit=10)         


i = 0
for h in headlines:
    print(h.text)
    link = h.find('a')
    print(link['href'])
    article = summaries[i].text
    print(article)
    i += 1    

for s in summaries:
    for h in headlines:
        print(h.text)
        link = h.find('a')
        print(link['href'])
        print(s.text)

