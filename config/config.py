# -*- coding: utf-8 -*-
# @Time    : 2024/01/18 4:02 PM
# @Author  : Pedro Anisio Silva
# @Email   : pedroanisio@arc4d3.com
# @File    : config.py

import os
import configparser
from datetime import timedelta

import redis


def get_config():
    """Retrieve configuration file"""
    conf = configparser.ConfigParser()
    flask_env = os.environ.get('FLASK_ENV')
    base_path = os.path.dirname(os.path.abspath(__file__)) + '/'

    default_env = {
        'config_path': base_path + 'dev.ini',
        'msg': 'Local configuration file: {}'.format(base_path + 'dev.ini'),
    }

    env_path_dict = {
        'default': default_env,
        'production': {
            'config_path': base_path + 'pro.ini',
            'msg': 'Production configuration file: {}'.format(base_path + 'pro.ini')
        },
    }
    env_obj = env_path_dict.get(flask_env, default_env)
    msg = env_obj.get('msg')
    config_path = env_obj.get('config_path')
    print(msg)
    conf.read(config_path)
    return conf


class BaseConfig:
    """Base configuration"""
    
    SECRET_KEY = 'change-me'  # Session encryption
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)  # Set session expiration time
    DEBUG = True
    # SERVER_NAME = 'example.com'
    RUN_HOST = '0.0.0.0'
    RUN_PORT = 9999

    @staticmethod
    def init_app(app):
        pass


class NewConfig(BaseConfig):
    """Configuration differentiation"""

    conf = get_config()  # Get the corresponding configuration file based on environment variables

    # Base
    SECRET_KEY = conf.get('base', 'SECRET_KEY')  # Session encryption
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)  # Set session expiration time
    DEBUG = conf.getboolean('base', 'DEBUG')
    RUN_HOST = conf.get('base', 'RUN_HOST')
    RUN_PORT = conf.getint('base', 'RUN_PORT')

    # MySQL
    MYSQL_USERNAME = conf.get('mysql', 'USERNAME')
    MYSQL_PASSWORD = conf.get('mysql', 'PASSWORD')
    MYSQL_HOSTNAME = conf.get('mysql', 'HOSTNAME')
    MYSQL_PORT = conf.getint('mysql', 'PORT')
    MYSQL_DATABASE = conf.get('mysql', 'DATABASE')
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        MYSQL_USERNAME,
        MYSQL_PASSWORD,
        MYSQL_HOSTNAME,
        MYSQL_PORT,
        MYSQL_DATABASE
    )
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Redis
    redis_obj = {
        'host': conf.get('redis', 'REDIS_HOST'),
        'port': conf.get('redis', 'REDIS_PORT'),
        'password': conf.get('redis', 'REDIS_PWD'),
        'decode_responses': conf.getboolean('redis', 'DECODE_RESPONSES'),
        'db': conf.getint('redis', 'REDIS_DB')
    }
    POOL = redis.ConnectionPool(**redis_obj)
    R = redis.Redis(connection_pool=POOL)


config_obj = {
    'production': None,
    'development': None,
    'default': NewConfig,
    'new': NewConfig
}

if __name__ == '__main__':
    print(config_obj['default'].DB_URI)
    print(config_obj['default'].DB_URI)
    print(config_obj['new'].DB_URI)
    print(config_obj['default'].R)
    print(config_obj['new'].R)

    print(config_obj['new'].RUN_HOST)
    print(config_obj['new'].RUN_PORT)
    print(config_obj['new'].DEBUG)
