from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create flask instance
app=Flask("__name__")

app.config["SQLALCHEMY_DATABASE_URI"]=""
app.config["SECRET_KEY"]="my secret key is Shubham Ghosh"

# Create a decorator initial 
@app.route("/")
def welcome():
    return render_template("index.html")

# Fileters
# safe - 
# capitalize - capitalize the value in html
# lower - lower case the value in html
# upper - upper case the value in html
# title - capitalize the every words in the value in html
# trim - removes the trailing spaces.
# striptags - removes the tags that the vaules

class NamerForm(FlaskForm):
    name=StringField("Whats your name?", validators=[DataRequired()])
    submit=SubmitField("Submit")
 
@app.route("/templat")
def templat():
    value = "Shubhams vaule"
    username = "Shubham Ghosh"
    age = 29
    menu = ["mango", "orange", "pizza", 32, 3.0, "coffee", "squids", "crabs", 2.0,]
    return render_template("index2.html", value=value, user_name= username, age=age, menu=menu)

# Create a decorator hello
@app.route("/hello/<user>")
def hello_world(user):
    return "<h1>hello {}</h1>".format(user)

# create name route
@app.route("/name", methods=["GET", "POST"])
def name():
    name= None
    form=NamerForm()
    if form.validate_on_submit():
        name= form.name.data
        form.name.data=''
    
    return render_template("name.html", name=name, form=form)

#Create custom error pages
#error route Invalid URL
@app.errorhandler(404)
def notfound(e):
    return render_template("error404.html")

#error route Internal server error URL
@app.errorhandler(500)
def internalServerError(e):
    return render_template("error500.html")

if(__name__=="__main__"):
    app.debug=True
    app.run()
