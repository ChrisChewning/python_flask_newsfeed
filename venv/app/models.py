from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#retrieves ID of user in session, and loads user into memory. 
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#UserMixin generic implementations. mixin is a class that contains methods for use by other classes without having to be the parent class of those other classes.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    articles = db.relationship('Article', backref='annotations', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#relationship is 1 to many. 1st arg is the many table. 
#backref defines the name of the field that points back to the one field. 
    def __repr__(self):
        return '<User {}>'.format(self.username)  




class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.String(500))
    url = db.Column(db.String(250))
    summary = db.Column(db.String(500))
    notes = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Article {}>'.format(self.article)

#repr method 'tells Python how to print objects of this class, which is useful for debugging.'

#User.articles has the initializes the User.articles field.
#This is not an actual field, but instead a 'high-level view of the relationship..."
#backref is an extra field. can't use a field you already have here. 
#lazy arg defines how the db query for relationship will be issued."