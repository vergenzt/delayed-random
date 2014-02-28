import bottle
import os
import requests
import uuid

queries = {}
random_fmt = 'http://www.random.org/integers/?' + '&'.join([
    'num=1',
    'min={min}',
    'max={max}',
    'col=1',
    'base=10',
    'format=plain',
    'rnd=new',
])

def random_int(min=0,max=10):
    response = requests.get(random_fmt.format(min=min,max=max))
    return int(response.content)

class Query(object):
    def __init__(self):
        self.qid = uuid.uuid4().hex
        self.val = random_int()


@bottle.route('/')
def index():
    ''' Display the new query form. '''
    return bottle.template('index.html', queries=queries)

@bottle.route('/newquery', method="POST")
def newquery():
    query = Query()
    queries[query.qid] = query
    return bottle.redirect('/query/{qid}'.format(qid=query.qid))

@bottle.route('/query/<qid:re:[0-9a-f]{32}>')
@bottle.view('query.html')
def query(qid):
    ''' Show a previously generated query. '''
    try:
        return {'query': queries[qid]}
    except KeyError:
        bottle.abort(404, 'Query not found')

if __name__=='__main__':
    port = int(os.environ.get('PORT', 8080))
    bottle.run(host='localhost', port=port, reloader=True)

app = bottle.default_app()

