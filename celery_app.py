# -*- coding: utf-8 -*-
# @Time    : 2024/01/18 4:02 PM
# @Author  : Pedro Anisio Silva
# @Email   : pedroanisio@arc4d3.com
# @File    : celery_app.py

from flask import Flask
from celery import Celery


def create_celery_app() -> Flask:
    """Instantiate a Flask application for Celery"""

    app = Flask(__name__)  # Create instance
    from ExtendRegister.conf_register import register_config
    from ExtendRegister.db_register import register_db
    register_config(app)  # Register configurations
    register_db(app)  # Register database
    return app


def create_celery(app: Flask) -> Celery:
    """
    Create and configure Celery instance
    :param app: Flask application instance
    :return: Configured Celery instance
    """

    celery_example = Celery(app.import_name)

    """
    Configuration Methods (Using Method 2 Here):
    1. Directly set configuration parameters:
       
        celery_example.conf.timezone = 'America/Sao_Paulo'
        celery_example.conf.broker_url = 'redis://...'
        celery_example.conf.result_backend = 'redis://...'
        ...
               
    2. Load Celery's independent configuration file (from config/celeryconfig.py):
       
        celery_example.config_from_object("config.celeryconfig")

    3. Load configurations from the Flask application instance.
       (Note: In Flask's configuration file, Celery-related settings must be lowercase, e.g., broker_url='redis://...')
       
        celery_example.conf.update(app.config)
    """

    celery_example.config_from_object("config.celeryconfig")

    # Attach Flask application context to Celery, allowing ORM models in tasks
    class ContextTask(celery_example.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_example.Task = ContextTask

    return celery_example


init_app = create_celery_app()
cel = create_celery(app=init_app)

"""
Run Celery in Foreground:
    celery --app=celery_app.cel worker -l INFO

Run Celery in Background:
    celery -A celery_app.cel multi start worker --pidfile="$HOME/run/celery/%n.pid" --logfile="$HOME/log/celery/%n%I.log"
    
Restart and Run in Background:
    celery -A celery_app.cel multi restart worker --pidfile="$HOME/run/celery/%n.pid" --logfile="$HOME/log/celery/%n%I.log"

Asynchronous Stop (Immediate Return):
    celery multi stop worker --pidfile="$HOME/run/celery/%n.pid"

Wait for Stop (Complete Pending Operations):
    celery multi stopwait worker --pidfile="$HOME/run/celery/%n.pid"
"""
