from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")    #[user].sites.tjhsst.edu/
def root():
    return render_template("index.html")
    
@app.route("/hello")   #[user].sites.tjhsst.edu/hello
def hello():
    return render_template("hello.html")