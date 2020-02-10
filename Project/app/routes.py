from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/edit')
def edit():
    return render_template("edit.html")

@app.route('/testing')
def testing():
    return render_template("experiment.html")

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form = form)