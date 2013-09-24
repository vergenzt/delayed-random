import flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
import os

app = flask.Flask(__name__)
app.debug = True
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__=='__main__':
    app.run()

