from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/edit')
def edit():
    return render_template("edit.html")

@app.route('/testing')
def testing():
    return render_template("experiment.html")