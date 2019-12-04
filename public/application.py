import os
import smtplib
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")    #[user].sites.tjhsst.edu/
def root():
    return render_template("index.html")
    
@app.route("/registrants")   #[user].sites.tjhsst.edu/registrants
def registrants():
    return render_template("registered.html", students=students)
    
@app.route("/register", methods=["POST"]) #[user].sites.tjhsst.edu/register
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    fav_class = request.form.get("class")
    if not name or not fav_class:
        return render_template("failure.html")
    message = "You are registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("coolcatvas@gmail.com", os.getenv("PASSWORD"))
    server.sendmail("coolcatvas@gmail.com", email, message)
    return render_template("success.html")