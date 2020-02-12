from flask import render_template, flash, redirect, url_for, make_response
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

@app.route('/edit/home')#, methods=['POST'])
def edit():
	resp = make_response(render_template('home.html'))
	resp.mimetype = 'text/plain'
	#return resp
	return render_template("edit.html")
