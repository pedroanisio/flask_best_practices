# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 4:43 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : restful_demo.py
# @Software: PyCharm

from all_reference import *


class RestfulDemoApi(Resource):
    """
    Flask RESTful demo
    """

    def get(self):
        data = {
            'time': time(),
            'datetime': datetime.now(),
            'current_process_id': os.getpid(),
            'parent_process_id': os.getppid(),
            'thread_id': threading.get_ident(),
            'db_id': id(db)
        }
        return api_result(code=200, message='Flask RESTful demo', data=data)

    def post(self):
        return api_result(code=200, message='Flask RESTful demo', data=[])


class DemoApi(Resource):
    """
    Parameter usage:
        If no parameters are passed in the URL, the default
        parameters page=1, size=10 will be used.
    """

    def get(self, page=1, size=10):
        return f'Flask RESTful GET parameters {page}, {size}'

    def post(self):
        return api_result(code=200, message='Flask RESTful POST')

    def put(self):
        return api_result(code=200, message='Flask RESTful PUT')

    def delete(self):
        return api_result(code=200, message='Flask RESTful DELETE')
