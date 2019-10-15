from flask import Flask #application object is instance of Flask
app = Flask(__name__) #set to the name of of the module where it's used. 
from app import routes

#this is for handling the app instance