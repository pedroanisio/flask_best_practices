# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 11:15
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : test_api.py
# @Software: PyCharm


from all_reference import *
from tasks.celery_tasks.task03 import test_orm


class TestMethodView(MethodView):
    """
    Test view demo
    """

    def get(self):
        """Test internal exception"""
        print(1 / 0)
        return

    def post(self):
        """Test custom exception"""
        return ab_code(666)


class TestRestful(Resource):
    """
    Test restful demo
    """

    def get(self):
        """Test internal exception"""
        print(1 / 0)
        return

    def post(self):
        """Test custom exception"""
        return ab_code_2(666)


class TestCeleryTask(MethodView):
    """
    Test asynchronous task
    """

    def get(self):
        """Test asynchronous task"""
        
        results = test_orm.delay()
        print(results)
        return api_result(
            code=200,
            message='Operation successful, check logs for execution result',
            data=[str(results)]
        )
