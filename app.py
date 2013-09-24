import bottle
import os

@bottle.route('/')
def index():
    return 'Hello, world!'

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    bottle.run(server='gunicorn', host='0.0.0.0', port=port)

