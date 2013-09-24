import flask
import os

app = flask.Flask(__name__)
app.config.update(*(
    DATABASE = '/tmp/flaskr.db',
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default',
))

@app.route('/')
def index():
    return 'Hello, world!'

if __name__=='__main__':
    app.run()

