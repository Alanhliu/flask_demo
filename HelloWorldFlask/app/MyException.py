from flask import request, jsonify
from werkzeug.exceptions import HTTPException


class MyException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake'
    error_code = 999

    def __init__(self, code=None, msg=None, error_code=None, header=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        super(MyException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_no_param()
        )

        return jsonify(body)