# -*- coding: utf-8 -*-
# @Time    : 2024/01/18 4:02 PM
# @Author  : Pedro Anisio Silva
# @Email   : pedroanisio@arc4d3.com
# @File    : bp_register.py


from app.api import restful_api, method_view_api
from app.controllers.other_module_01.module_01 import route_module_01
from app.controllers.other_module_02.module_02 import route_module_02
from app.controllers.other_module_03.module_03 import route_module_03


def register_bp(app):
    """Blueprint registration"""

    """API Blueprint"""
    app.register_blueprint(restful_api, url_prefix="/api")

    """CMS Blueprint"""
    app.register_blueprint(method_view_api, url_prefix="/cms")

    """Other Independent Blueprint Registration"""	
    app.register_blueprint(route_module_01, url_prefix="/m1")
    app.register_blueprint(route_module_02, url_prefix="/m2")
    app.register_blueprint(route_module_03, url_prefix="/m3")
