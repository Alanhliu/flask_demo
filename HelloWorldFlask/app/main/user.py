# from flask import render_template, redirect, url_for
from . import main


@main.route('/user/<string:username>')
def user(username=None):
    return 'User name is %s' % username


@main.route('/user/<int:user_id>')
def user_by_id(user_id=None):
    return 'User id is %d' % user_id


@main.route('/user/info', methods=['POST'])
def user_info():
    return "user sex:man"


@main.before_request
def before_request():
    print('before_request')
