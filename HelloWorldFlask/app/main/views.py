from flask import render_template, redirect, url_for
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/introduce')
def introduce():
    return redirect(url_for('.home'))


@main.route('/welcome')
def welcome():
    return redirect(url_for('auth.mysite'))