from flask import render_template, url_for, request
from app import app, db #import app variable, which is a member of the app package
from app.forms import LoginForm, RegistrationForm
from flask import Flask, render_template, redirect, flash, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2
from datetime import date
from app.models import User, Article
from flask_login import current_user, login_user, logout_user



source = requests.get('https://www.washingtonpost.com/').text
soup = BeautifulSoup(source, 'lxml')

front_page = soup.find("section", {"id": "main-content"})
articles = front_page.findAll(True, {'class':['headline x-small normal-style text-align-inherit', 'headline small normal-style text-align-inherit', 'headline xx-small normal-style text-align-inherit']})
                                                                                                                  


@app.route('/', methods=['GET', 'POST'])
def index():
    print('heeeeyyyyy-ooooo')
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
            link = article.find('a')
            summary = article.find_next_sibling("div")
            a['link_text'] = link.text
            a['link_url'] = link['href']
            
            # article = Article(article=article(link.text))
            # db.session.add(article)
            # db.session.commit()
            # flash('Saved')


            if summary:
                a['link_summary'] = summary.text
            else:
                a['link_summary'] = 'No summary given'
            waPo_articles.append(a)

            
        else: 
            break

        # foo = request.form['s_article']
        # print(foo)

    # if request.method == 'POST':
    #     article = Article(article=link.text)
    #     db.session.add(article)
    #     db.session.commit()
    #     flash('Saved')
    #     #return redirect("/")
    # test = request.args['save_article']
    # print(test)

    return render_template('index.html', waPo_articles= waPo_articles, today_str= today_str)



# @app.route('/save', methods=['POST'])
# def save():
#     saved = request.form['save_article']
#     print(saved, ' saved me!')
    
#     return render_template('index.html')



@app.route('/save', methods=['POST'])
def save():
    saved = request.form['save_article']
    print(saved, ' saved me!')
    if request.method == 'POST':
        article = Article(article=saved) #should say Testing
        db.session.add(article)
        db.session.commit()
        flash('Saved')
    return redirect(url_for('index'))





@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        #query the db. filter by only includes object w. matching username. there will be 0 or 1 result (first())
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        #else call the login_user fn from Flask-Login
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm() #instatiates it
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)