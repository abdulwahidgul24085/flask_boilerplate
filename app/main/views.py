from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('index.html',)