# -*- coding: utf-8 -*-
# @Time    : 2024/01/18 4:02 PM
# @Author  : Pedro Anisio Silva
# @Email   : pedroanisio@arc4d3.com
# @File    : ApplicationExample.py

import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from ExtendRegister.command_register import register_commands  # Commands
from ExtendRegister.conf_register import register_config  # Configuration
from ExtendRegister.excep_register import errors  # Global Exception Registration
from ExtendRegister.hook_register import register_hook  # Interceptor Registration
from ExtendRegister.bp_register import register_bp  # Blueprint Registration
from ExtendRegister.db_register import register_db, db  # Database Registration
from ExtendRegister.model_register import *  # Models

template_folder = os.getcwd() + '/app/templates'
static_folder = os.getcwd() + '/app/static'


def create_app():
    """Application Instance"""

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)  # Create Instance
    CORS(app, supports_credentials=True)  # Enable Cross-Origin Resource Sharing (CORS)
    register_commands(app)  # Register Flask CLI Commands
    register_config(app)  # Register Configuration
    register_hook(app)  # Register Interceptors (Must be before Blueprint)
    register_bp(app)  # Register Blueprints
    register_db(app)  # Register Database
    Migrate(app, db)  # Enable ORM Migrations
    return app
