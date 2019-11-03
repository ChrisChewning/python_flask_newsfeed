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
source2 = requests.get('https://www.nytimes.com/').text
source3 = requests.get('https://www.statesman.com/').text

#WASHINGTON POST
soup = BeautifulSoup(source, 'lxml')
front_page = soup.find("section", {"id": "main-content"})
articles = front_page.findAll(True, {'class':['headline x-small normal-style text-align-inherit', 'headline small normal-style text-align-inherit', 'headline xx-small normal-style text-align-inherit']})

#NY TIMES
soup2 = BeautifulSoup(source2, 'lxml')
front_page2 = soup2.find("main", {"id": "site-content"})                                                         
nytimes = front_page2.findAll(True, {'class':['css-6p6lnl', 'css-omcqsq' ]})[:11]  #class_='css-6p6lnl'.split())  #css-qvz0vj eqveam61  #css-1ez5fsm esl82me1
# print(nytimes, '<-- this is nytimes')
#AUSTIN AMERICAN STATESMAN 
soup3 = BeautifulSoup(source3, 'lxml')
front_page3 = soup3.find("section", {"id": "featured"})  #gets the main page. 
aas = front_page3.findAll("article", {"class": "summary"})
# print(aas, ' <-- this is aas')



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

    for nyta in nytimes:
        b = { }
        if nyta.h2 is None:
            continue  
        elif count <20: 
            count +=1
        b['link_text'] = nyta.h2.text        
        b['link_url'] = ("{}{}".format('https://www.nytimes.com', nyta.find('a')['href']))        
        summary = nyta.find('p')
        if summary == None:
            b['link_summary'] = 'No Summary' #print('No summary')
        else: 
            b['link_summary'] = summary.text       
        # if count ==20:
        #     break

        waPo_articles.append(b)
        print(nyta, '<-- this is nyta')
        # print(waPo_articles)

    for aas_article in aas:
        c = { } 
        c['link_text'] = aas_article.span.text
        c['link_url'] = aas_article.find('a')['href']
        # c['summary'] = aas_article.span.text
        count +=1
        if count >=30:
            break
        waPo_articles.append(c)
        print(c, ' <-- this is c')
        
    return render_template('index.html', waPo_articles=waPo_articles, today_str=today_str)




@app.route('/save', methods=['POST'])
def save():
    save_article = request.form['save_article']
    save_url = request.form['save_url']
    save_summary = request.form['save_summary']
    if request.method == 'POST':
        new_row = Article(article = save_article, summary = save_summary, url = save_url, user_id = current_user.id)
        db.session.add(new_row)
        db.session.commit()
        flash('Saved')
    return redirect(url_for('index'))


@app.route('/myaccount', methods=['GET', 'POST'])
@login_required
def myaccount():
    article_list = db.session.query(Article).filter(Article.article != None, Article.user_id == current_user.id)
    article_url = db.session.query(Article).filter(Article.url != None, Article.user_id == current_user.id)
    article_notes = db.session.query(Article).filter(Article.user_id == current_user.id)
    return render_template('myaccount.html', article_list = article_list, article_url = article_url)


@app.route('/add_note', methods=['GET', 'POST'])
@login_required
def add_note():
    add_note = request.form.get("add_note") #get the new note. ex: 'hello'
    add_id = request.form.get("add_id") #get the id of the current object. 14
    add = db.session.query(Article).filter(Article.id == add_id).\
        update({Article.notes: add_note}) #ties the change to the session.
    db.session.commit()
    return redirect(url_for('myaccount'))

@app.route('/edit_note', methods=['GET', 'POST'])
@login_required
def edit_note():
    edit_note = request.form.get("edit_note") #get the new note. 
    print(edit_note, " <-- edit note")
    edit_note_id = request.form.get("edit_note_id") #get the id of the current object. 14
    print(edit_note_id, " <-- edit note id")
    edit = db.session.query(Article).filter(Article.id == edit_note_id).\
        update({Article.notes: edit_note}) #ties the change to the session.
    db.session.commit()
    return redirect(url_for('myaccount'))

@app.route('/delete_note', methods=['GET', 'POST'])
@login_required
def delete_note():
    delete_note = request.form.get("delete_note") #get the new note. 
    print(delete_note, " <-- delete note")
    delete_note_id = request.form.get("delete_note_id") #get the id of the current object. 14
    print(delete_note_id, " <-- delete note id")
    edit = db.session.query(Article).filter(Article.id == delete_note_id).\
        update({Article.notes: None}) 
    db.session.commit()
    return redirect(url_for('myaccount'))




@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    delete_row = request.form['delete_row']  #.get('delete_row') would work also. 
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




