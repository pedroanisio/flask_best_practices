# -*- coding: utf-8 -*-
# @Time    : 2024/01/18 4:02 PM
# @Author  : Pedro Anisio Silva
# @Email   : pedroanisio@arc4d3.com
# @File    : api_result.py
from flask import jsonify


# Response format

def api_result(code=None, message=None, data=None, details=None, status=None):
    """
    Generate a standardized API response.

    :param code: Response status code
    :param message: Response message
    :param data: Response data payload
    :param details: Additional details (not currently used)
    :param status: HTTP status (not currently used)
    :return: JSON response
    """
    result = {
        "code": code,
        "message": message,
        "data": data,
    }

    if not result['data']:
        result.pop('data')
    
    return jsonify(result)
