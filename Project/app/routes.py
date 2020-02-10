from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/all')
def all():
    return render_template("all.html")
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title = 'Sign In', form = form)