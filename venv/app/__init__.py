from flask import Flask #application object is instance of Flask
app = Flask(__name__) #set to the name of of the module where it's used. needs to be above from app...
from app import routes
from flask_bootstrap import Bootstrap

Bootstrap(app)

app.config['SECRET_KEY'] = 'ooglyboogly'

#this is for handling the app instance