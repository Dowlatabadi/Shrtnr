from flask import Flask
from flask import request, jsonify

alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_dict={x:i for i,x in enumerate(alph)}

def encode(input_int):
    res=[]
    if input_int==0:
        return alph[0]
    while input_int>0:
        r=input_int%(len(alph))
        res.append(alph[r])
        input_int//=len(alph)
    return ''.join(reversed(res))

def decode(input_str):
    res=0
    for x in input_str:
        res=alph_dict[x]+(res*len(alph))
    return res
def redis_short():
    offset=1000000
    import redis

    r = redis.Redis(
    host='redis',
    port=6379, )
    #r.set('foo', 'bar')
    value = r.get('Counter')
    if value==None:
        r.set('Counter',0)
    r.incr('Counter',1)
    value = r.get('Counter')
    shrt=encode(int(value)+offset)
    return shrt
def set(url):
    import redis
    r = redis.Redis(
    host='redis',
    port=6379, )
    saved_short=r.get(url)
    if saved_short!=None:
        return 'exmple.com/'+saved_short.decode('utf-8')
    shrt=redis_short()
    #r.set('foo', 'bar')
    r.set(shrt,url)
    r.set(url,shrt)
    return 'exmple.com/'+shrt
def get(shrt):
    import redis
    r = redis.Redis(
    host='redis',
    port=6379, )
    link=r.get(shrt)
    if link==None:
        return "not found"
    return link.decode('utf-8')

app = Flask(__name__)


@app.route('/shortURL/', methods=['POST'])
def set_url():
    data = request.form
    URL = request.values.get('URL')
    shrt=set(URL)
    return jsonify({
'message':'success',
'URL':shrt,})

@app.route('/getURL/<shrt>', methods=['GET', 'POST'])
def get_url(shrt):
    link=get(shrt)
    return jsonify({
'message':'success',
'URL':link,})
    

if __name__ == '__main__':
      app.run(host='localhost', port=1025)
