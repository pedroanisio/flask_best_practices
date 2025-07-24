# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 5:21 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : hook_register.py

from app.api import restful_api, method_view_api
from common.interceptors.ApiHook import api_before_request, api_after_request
from common.interceptors.CmsHook import crm_before_request, crm_after_request
from common.interceptors.AppHook import app_before_request, app_after_request


def register_hook(app):
    """Interceptor (Hook Function) Registration"""

    restful_api.before_request(api_before_request)
    restful_api.after_request(api_after_request)

    method_view_api.before_request(crm_before_request)
    method_view_api.after_request(crm_after_request)

    # app.before_request(app_before_request)
    # app.after_request(app_after_request)
