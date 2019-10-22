from flask import Flask #application object is instance of Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__) #set to the name of of the module where it's used. needs to be above from app...
app.config.from_object(Config)
login = LoginManager(app) #manages state & 'remember me'

Bootstrap(app)
app.config['SECRET_KEY'] = 'ooglyboogly'  #to persist login
db = SQLAlchemy(app)  #to set a database object
migrate = Migrate(app, db)  #for migrations

from app import routes, models


#this is for handling the app instance
#db is represented by the db instance here. you also have the db migration engine instance below that line.
