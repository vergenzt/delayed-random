import bottle
import os

@bottle.route('/')
def index():
    return 'Hello, world!'

if __name__=='__main__':
    port = int(os.environ.get('PORT', 8080))
    bottle.run(host='localhost', port=port)

app = bottle.default_app()

