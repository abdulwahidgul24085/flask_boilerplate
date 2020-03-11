from app import app
from flask import redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    return "<h1>This is the Index Func</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # include login form
    # if login form validated
    # query users by username or email
    # if user doesn't exists or pass doesn't match flash a message for bad creds and redirect to login page
    # login_user(url_for('login'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page) != '':
            next_page = url_for('index')
        return redirect(next)
    return 'Login Page'

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))