from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from app.forms import LoginForm
from flask import render_template
from app import app

user = {}

@app.route('/')
@app.route('/index')
def index():
    user['username'] = 'atulit'
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.j2', user= user, posts= posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me= {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.j2', title='Sign In', form=form)
