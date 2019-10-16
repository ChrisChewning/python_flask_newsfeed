from app import app 
from flask import Flask, render_template
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2


source = requests.get('https://www.washingtonpost.com/').text
#lxml is the markup
soup = BeautifulSoup(source, 'lxml')

front_page = soup.find("section", {"id": "main-content"})
articles = front_page.findAll(True, {'class':['no-skin flex-item flex-stack normal-air text-align-left wrap-text equalize-height-target', 'no-skin flex-item flex-stack normal-air text-align-left equalize-height-target', 'art art-high art-small-lg art-small-md art-small-sm art-small-xs enforce-max art-full-width text-align-left no-extra-rule']}, limit=10)

def getWaPo():
    l = []
    for article in articles:
        a = { }
        link = article.find('a')
        a['link_text'] = link.text 
        a['link_url'] = link['href']
        # print(a['link_text'])
        # print(a['link_url'])
        print(a)
        if article.find(class_="blurb normal normal-style"):
            a['link_summary'] = article.text
        else:
            a['link_summary'] = 'No summary given'
        l.append(a)
    return l
    
    div:first-child'



#this grabs the summary without the extra information:

# headline_text = front_page.findAll(class_='blurb normal normal-style', limit=10)
    # for h in headline_text:
#     print(h.text)

