from flask import Flask
from redis import Redis,RedisError
#a redis instance, from connection to redis -server
redis = Redis(host="redis-server",db=0)

#a flask application instance using Flask constructor
app=Flask(__name__)

#defining my own routes
@app.route('/')
def hello():
    return "<h1> Hello World </h1>"

@app.route('/visit')
def incr_counter():
    try :
        visits = redis.incr("counter")
    except:
        visit="<i> redis server not available </i>"
    html = "<h1> Number of visits : {}</h1>".format(visits)
    return html

if __name__=="__main__":
    app.run(debug=True,port=80,host="0.0.0.0")