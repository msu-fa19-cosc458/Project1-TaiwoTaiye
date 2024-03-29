# app.py
import flask
import os

app = flask.Flask(__name__)

@app.route('/') 
def index(): 
    return flask.render_template("index.html")
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)