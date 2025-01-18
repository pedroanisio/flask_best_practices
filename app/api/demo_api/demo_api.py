# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 11:34
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : demo_api.py
# @Software: PyCharm

from flask import request

from all_reference import *


class MethodViewParams(MethodView):
    """
    MethodView - Retrieve GET request parameters
    """

    def get(self):
        """Retrieve GET request parameters"""

        # Method 1: Retrieve individually
        a = request.args.get('a')
        b = request.args.get('b')
        print(a, b)

        # Method 2: Retrieve all at once
        data = request.args.to_dict()
        print(data)
        return api_result(code=200, 
                          message='MethodView - Retrieved GET parameters', 
                          data=data)


class MethodViewFormData(MethodView):
    """
    MethodView - Retrieve form-data parameters
    """

    def post(self):
        """Retrieve form-data parameters"""

        # Method 1: Retrieve individually
        a = request.form.get('a')
        b = request.form.get('b')
        print(a, b)

        # Method 2: Retrieve all at once
        data = request.form.to_dict()
        print(data)
        a = data.get('a')
        b = data.get('b')
        print(a, b)
        return api_result(code=200, 
                          message='MethodView - Retrieved form-data parameters', 
                          data=data)


class MethodViewJson(MethodView):
    """
    MethodView - Retrieve JSON parameters
    """

    def post(self):
        """Retrieve JSON parameters"""

        data = request.get_json()
        d1 = data.get('d1')
        d2 = data.get('d2')
        d3 = data.get('d3')
        print(d1)
        print(d2)
        print(d3)
        return api_result(code=200, 
                          message='MethodView - Retrieved JSON parameters', 
                          data=data)


class MethodViewBytesData(MethodView):
    """
    MethodView - Retrieve binary data parameters
    """

    def post(self):
        """Retrieve binary data parameters"""

        data = request.get_data()
        print(data)
        print(type(data))
        return api_result(code=200, 
                          message='MethodView - Retrieved binary data parameters', 
                          data=f"Data is {type(data)}")
