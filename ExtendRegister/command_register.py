# -*- coding: utf-8 -*-
# @Time    : 2024/01/18 4:02 PM
# @Author  : Pedro Anisio Silva
# @Email   : pedroanisio@arc4d3.com
# @File    : command_register.py

import os
import click
import shutil

from common.libs.db import project_db
from ExtendRegister.db_register import db
from app.models.admin.models import Admin, Role, Permission

"""
export FLASK_APP=ApplicationExample.py
"""

def register_commands(app):
    """Flask CLI Commands"""

    @app.cli.command("hello_world", help='Hello World')
    def hello_world():
        print('Hello World')

    @app.cli.command(help='Initial ORM operations')
    def orm():

        migrations_path = os.getcwd() + "/migrations"

        if os.path.exists(migrations_path):
            shutil.rmtree(migrations_path)
            print(f'>>> Migrations deleted: {migrations_path}')
        else:
            print(f'>>> Migrations not found: {migrations_path}')

        try:
            drop_table_sql = """DROP TABLE IF EXISTS alembic_version;"""
            print(drop_table_sql)
            drop_result = project_db.execute_sql(sql=drop_table_sql)
            print(f'>>> Drop result: {drop_result}')
        except BaseException as e:
            print(f'>>> Failed to delete alembic_version: {e}')

        try:
            os.system("flask db init")
            os.system("flask db migrate")
            os.system("flask db upgrade")
            print('>>> Creation successful')
        except BaseException as e:
            print(f'>>> Creation failed: {e}')

    @app.cli.command(help='Update database tables')
    def table():
        try:
            os.system("flask db migrate")
            os.system("flask db upgrade")
            print('>>> Update successful')
        except BaseException as e:
            print(f'>>> Update failed: {e}')

    @app.cli.command(help='Create user roles and permissions')
    def crm():
        try:
            user = Admin.query.filter_by(username='admin').first()
            if user:
                pass
            else:
                user = Admin(username='admin', password='123456')
                db.session.add(user)
                db.session.commit()
                print('CMS user added successfully')
            for r in range(1, 5):
                role_obj = Role(name=f'Role {r}')
                db.session.add(role_obj)
            db.session.commit()
            print('CMS roles added successfully')

            for p in range(1, 5):
                permission_obj = Permission(name=f'Permission {p}')
                db.session.add(permission_obj)
            db.session.commit()
            print('CMS permissions added successfully')
        except BaseException as e:
            print(f'Error: {e}')

    @app.cli.command("create_user", help="Create a user")
    @click.option("--username", help="Username", type=str)
    @click.option("--password", help="Password", type=str)
    def create_user(username, password):
        """
        Command: flask create-user --username yyx --password 123456
        """
        
        query_user = Admin.query.filter_by(username=username).first()
        if query_user:
            print(f'>>> User: {username} already exists')
        else:
            user = Admin(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            print(f'User: {username} added successfully')
