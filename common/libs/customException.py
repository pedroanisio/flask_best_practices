# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 2:46 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : customException.py
# @Software: PyCharm

from werkzeug.exceptions import HTTPException
from flask import jsonify, abort, request
import flask_restful

custom_resp_dict = {
    333: 'Test custom exception',
    400: 'Parameter type error',
    401: 'Unauthorized - Token expired',
    403: 'No permission',
    500: 'Server error',
    666: 'Token?',
    996: 'No hope left'
}


class CustomException(HTTPException):
    code = None
    msg = None

    def __init__(self, code=None, msg=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        super(CustomException, self).__init__(self.code, self.msg)


def method_view_ab_code(code):
    """MethodView custom exception"""
    msg = custom_resp_dict.get(code, 'ERROR')
    raise CustomException(code=code, msg=msg)


def flask_restful_ab_code(code):
    """Flask Restful custom exception"""
    message = custom_resp_dict.get(code)
    if message:
        req = request.method + ' ' + request.path
        result = {
            "code": code,
            "message": message,
            "request": req
        }
        result = jsonify(result)
    else:
        result = code
    # Modify and simplify flask_restful.abort
    flask_restful.abort = abort(result)
    flask_restful.abort(code)
