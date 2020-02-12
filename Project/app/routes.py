from flask import render_template, flash, redirect, url_for, make_response
from app import app
from app.forms import LoginForm
from os import listdir
from os.path import isfile, join

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/all')
def all():
    mypath = '/Users/sgb7/Desktop/Bin/Basic-Flask-Website/Project/app/templates'
    pages = [f for f in listdir(mypath) if isfile(join(mypath,f))]
    return render_template("all.html", pages=pages)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title = 'Sign In', form = form)

@app.route('/edit/<page_name>')
def edit(page_name):
	return render_template("edit.html", page_name = render_template(page_name + '.html'))


