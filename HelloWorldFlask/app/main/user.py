# from flask import render_template, redirect, url_for
from . import main
from ..models import User
from app import db
from flask import request, json, jsonify, abort, make_response
from app import MyException


@main.route('/user/<string:username>')
def user(username=None):
    return 'User name is %s' % username


@main.route('/user/list')
def user_list():
    users = User.query.all()
    abort(401)
    # raise MyException(100, 1000, 'do it')
    print(users)
    list = []
    for user in users:
        print(user.__dict__)
        print(dict(user.__dict__))
        list.append(user.as_dict())

    # response = make_response(jsonify(response=list))
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Methods'] = 'POST'
    # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    # return response

    # return jsonify(dict('response', list))
    return jsonify(list)




@main.route('/user', methods=['POST'])
# @main.route('/user/create')
def user_create():
    # user = User('iron man', '123456')
    username = request.form['username']
    password = request.form['password']
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
    return '插入'


# @main.route('/user', methods=['DELETE'])
@main.route('/user/delete')
def user_delete():
    # user = User.query.filter(User.uid == 102).first()
    # db.session.delete(user)

    # 主页 '**' 和 '*'
    # filter_by用于查询简单的列名，不支持比较运算符。
    # filters = {'uid': 101}
    # User.query.filter_by(**filters).delete()

    # filter比filter_by的功能更强大，支持比较运算符，支持or_、in_等语法。
    # User.query.filter(User.uid == 103).delete()

    filters = {
        User.uid == 1
    }
    User.query.filter(*filters).delete()

    db.session.commit()
    return '删除'


# @main.route('/user', methods=['DELETE'])
@main.route('/user/update')
def user_update():
    user = User.query.filter(User.uid == 2).first()
    user.password = "123456"
    db.session.commit()
    return "更新"


@main.route('/user/<int:user_id>')
def user_by_id(user_id=None):
    return 'User id is %d' % user_id


@main.route('/user/info', methods=['POST'])
def user_info():
    return "user sex:man"


@main.before_app_request
def before_request():
    print('before_request')


@main.app_errorhandler
def error(error):
    response = dict(status=0, message="404 Not Found")
    return jsonify(response), 404