# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 5:37 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : method_view_demo.py
# @Software: PyCharm

from all_reference import *


class MethodViewDemo(MethodView):
    """
    Method View Demo
    """

    def get(self, page=1, size=10):
        return api_result(code=200, message=f'MethodView GET. Params: {page},{size}')

    def post(self):
        return api_result(code=200, message='MethodView POST')

    def put(self):
        return api_result(code=200, message='MethodView PUT')

    def delete(self):
        return api_result(code=200, message='MethodView DELETE')
