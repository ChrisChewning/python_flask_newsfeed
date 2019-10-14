from flask import Flask, render_template
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2


source = requests.get('https://www.washingtonpost.com/').text
#lxml is the markup
soup = BeautifulSoup(source, 'lxml')

front_page = soup.find("section", {"id": "main-content"})
articles = front_page.findAll(True, {'class':['no-skin flex-item flex-stack normal-air text-align-left wrap-text equalize-height-target', 'no-skin flex-item flex-stack normal-air text-align-left equalize-height-target']}, limit=10)       


for article in articles:
    link = article.find('a')
    link_text = link.text
    link_url = link['href']
    print(link_text)
    print(link_url)

    if article.find(class_="blurb normal normal-style"):
        print(article.text)
    else:
        print("No summary given")
    

#this grabs the summary without the extra information:

# headline_text = front_page.findAll(class_='blurb normal normal-style', limit=10)
    # for h in headline_text:
#     print(h.text)

