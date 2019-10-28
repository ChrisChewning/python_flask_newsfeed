from flask import render_template, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask import Flask, render_template, redirect, flash, jsonify
from bs4 import BeautifulSoup, SoupStrainer
import requests  #from python library
import urllib.request as urllib2
from datetime import date
from app.models import User, Article
from flask_login import current_user, login_user, logout_user, login_required


source = requests.get('https://www.washingtonpost.com/').text
soup = BeautifulSoup(source, 'lxml')

front_page = soup.find("section", {"id": "main-content"})
articles = front_page.findAll(True, {'class':['headline x-small normal-style text-align-inherit', 'headline small normal-style text-align-inherit', 'headline xx-small normal-style text-align-inherit']})
                                                                                                                  


@app.route('/', methods=['GET', 'POST'])
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




@app.route('/save', methods=['POST'])
def save():
    save_article = request.form['save_article']
    save_url = request.form['save_url']
    if request.method == 'POST':
        new_row = Article(article = save_article, url=save_url, user_id = current_user.id)
        db.session.add(new_row)
        db.session.commit()
        flash('Saved')
    return redirect(url_for('index'))


@app.route('/myaccount', methods=['GET', 'POST'])
@login_required
def myaccount():
    article_list = db.session.query(Article).filter(Article.article != None, Article.user_id == current_user.id)
    article_url = db.session.query(Article).filter(Article.url != None, Article.user_id == current_user.id)

    return render_template('myaccount.html', article_list = article_list, article_url = article_url)



@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    delete_row = request.form['delete_row']  #.get('delete_row') would work also. 
    print(delete_row, ' <-- this is delete row')
    delete = Article.query.filter_by(id=delete_row).first()
    print(delete)
    db.session.delete(delete)
    db.session.commit()

    return redirect(url_for('myaccount'))




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




