import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



    #SQLALCHEMY extension gets the location of the  OR app.db in your base directory.
    #Track Modifications is false so it doesn't "signal the application every time a change is ab to be made in the db"
    #SQLite has each db stored in a single file on a disk. No need to run db server.
