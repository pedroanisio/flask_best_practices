# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 7:52 PM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : db.py
# @Software: PyCharm

import json
import decimal
from datetime import datetime

import pymysql

from config.config import config_obj

CONFIG_OBJ = config_obj.get('new')

R = CONFIG_OBJ.R  # Redis instance

DB = {
    'user': CONFIG_OBJ.MYSQL_USERNAME,
    'password': CONFIG_OBJ.MYSQL_PASSWORD,
    'host': CONFIG_OBJ.MYSQL_HOSTNAME,
    'port': CONFIG_OBJ.MYSQL_PORT,
    'db': CONFIG_OBJ.MYSQL_DATABASE
}


class MyPyMysql:
    def __init__(self, host=None, port=None, user=None, password=None,
                 db=None, debug=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.debug = debug

    def db_obj(self):
        """Return database object"""
        try:
            database_obj = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db)
            return database_obj
        except BaseException as e:
            return f'Error connecting to database: {str(e) if self.debug else ""}'

    def execute_sql(self, sql=None):
        """Execute a raw SQL command"""
        try:
            db = self.db_obj()
            with db.cursor() as cur:
                result = cur.execute(sql)
                return result
        except BaseException as e:
            print(str(e))

    def select(self, sql=None, only=None, size=None):
        """Perform a SQL SELECT query"""
        def __format_result(r):
            if isinstance(r, list):
                return [self._format_record(i) for i in r]
            elif isinstance(r, dict):
                return self._format_record(r)
            return r

        try:
            db = self.db_obj()
            with db.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute(sql)
                if only and not size:
                    return __format_result(cur.fetchone())
                if size and not only:
                    return __format_result(cur.fetchmany(size))
                return __format_result(cur.fetchall())
        except BaseException as e:
            return f'select: Error occurred: {str(e) if self.debug else ""}'

    def _format_record(self, record):
        """Format individual record values"""
        formatted_record = {}
        for k, v in record.items():
            if isinstance(v, decimal.Decimal):
                formatted_record[k] = float(v)
            elif isinstance(v, datetime):
                formatted_record[k] = str(v)
            else:
                formatted_record[k] = v
        return formatted_record

project_db = MyPyMysql(**DB, debug=CONFIG_OBJ.DEBUG)  # MySQL instance

if __name__ == '__main__':
    print('\n=== Test MySQL ===')
    sql = "SELECT id, username FROM crm_user WHERE id=1;"
    print('Ping:', project_db.db_obj().open)
    result = project_db.select(sql, only=True)
    print(result)

    print('\n=== Test Redis ===')
    print('Ping:', R.ping())
    print(R.get('yangyuexiong'))
