# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 11:03 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
from flask_restful import Api

from .restful_demo.restful_demo import RestfulDemoApi, DemoApi
from .method_view_demo.method_view_demo import MethodViewDemo
from .demo_api.demo_api import MethodViewParams, MethodViewJson, MethodViewFormData, MethodViewBytesData
from .route_demo.route_demo import module_01_index
from .test_api.test_api import TestRestful, TestMethodView, TestCeleryTask

method_view_api = Blueprint('cms', __name__)
restful_api = Blueprint('api', __name__)
api = Api(restful_api)

"""
Flask RESTful route registration
Registering URL with and without parameters
Without parameters: http://0.0.0.0:9999/api/demo
With parameters: http://0.0.0.0:9999/api/demo/123/456
"""
api.add_resource(DemoApi, '/demo', '/demo/<page>/<size>', endpoint='demo')
api.add_resource(RestfulDemoApi, '/', endpoint='restful_demo_api')
api.init_app(restful_api)

"""
Method View class-based route registration
URLs with parameters need to be registered separately
Without parameters: http://0.0.0.0:9999/cms/demo
With parameters: http://0.0.0.0:9999/cms/demo/999/888
"""
method_view_api.add_url_rule('/', view_func=MethodViewDemo.as_view('demo_get'))
method_view_api.add_url_rule('/demo', view_func=MethodViewDemo.as_view('demo_post'))
method_view_api.add_url_rule('/demo/<page>/<size>/', view_func=MethodViewDemo.as_view('demo_param'))

"""
Examples of obtaining request parameters (similar to Flask RESTful, shown here using MethodView)
"""
method_view_api.add_url_rule('/mv_params', view_func=MethodViewParams.as_view('mv_params'))
method_view_api.add_url_rule('/mv_json', view_func=MethodViewJson.as_view('mv_json'))
method_view_api.add_url_rule('/mv_form_data', view_func=MethodViewFormData.as_view('mv_form_data'))
method_view_api.add_url_rule('/mv_bytes_data', view_func=MethodViewBytesData.as_view('mv_bytes_data'))

"""
Route registration
"""
method_view_api.add_url_rule('/m1', methods=["GET", "POST"], endpoint='module_01_index', view_func=module_01_index)

"""
Static file handling/access methods
http://0.0.0.0:9999/static/flask.jpg
http://0.0.0.0:9999/static/images/flask.jpg
"""

"""
Testing global exceptions
"""
api.add_resource(TestRestful, '/test_restful_ex', endpoint='test_restful_ex')
method_view_api.add_url_rule('/test_mv_ex', view_func=TestMethodView.as_view('test_mv_ex'))
method_view_api.add_url_rule('/test_celery', view_func=TestCeleryTask.as_view('test_celery'))


@method_view_api.route('/<path:path>/images')
def static_file(path):
    return method_view_api.send_static_file(path)
