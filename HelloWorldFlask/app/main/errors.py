from flask import render_template, jsonify, request, make_response
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404


@main.app_errorhandler(401)
def user_auth_failed(e):
    print(request.headers.get("token"))
    response = dict(status=401, message="user auth failed")
    return jsonify(response), 401


@main.app_errorhandler(405)
def method_not_allowed(e):
    response = dict(status=e.code, message=e.name)
    return jsonify(response), e.code