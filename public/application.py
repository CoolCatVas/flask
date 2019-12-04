from flask import Flask, redirect, render_template, request

app = Flask(__name__)

#Registered students
students = []

@app.route("/")    #[user].sites.tjhsst.edu/
def root():
    return render_template("index.html")
    
@app.route("/registrants")   #[user].sites.tjhsst.edu/registrants
def registrants():
    return render_template("registered.html", students=students)
    
@app.route("/register", methods=["POST"]) #[user].sites.tjhsst.edu/register
def register():
    name = request.form.get("name")
    fav_class = request.form.get("class")
    if not name or not fav_class:
        return render_template("failure.html")
    students.append("{} who likes {}".format(name, fav_class))
    return redirect("/registrants")
    