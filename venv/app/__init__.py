from flask import Flask #application object is instance of Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) #set to the name of of the module where it's used. needs to be above from app...
app.config.from_object(Config)

from app import routes
from flask_bootstrap import Bootstrap

Bootstrap(app)
app.config['SECRET_KEY'] = 'ooglyboogly'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


#this is for handling the app instance
#db is represented by the db instance here. you also have the db migration engine instance below that line.
