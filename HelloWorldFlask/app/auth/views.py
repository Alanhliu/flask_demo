from flask import render_template
from . import auth


@auth.route('/mysite')
def mysite():
    return render_template('home.html')


@auth.route('/welcome')
def welcome():
    return 'welcome'
