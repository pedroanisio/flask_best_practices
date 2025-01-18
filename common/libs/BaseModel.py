# -*- coding: utf-8 -*-
# @Time    : 2019-05-16 17:06
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : BaseModel.py
# @Software: PyCharm

import json
import decimal
import warnings
import time
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.dialects.mysql import BIGINT, TINYINT

from ExtendRegister.db_register import db


class BaseModel(db.Model):
    """
    id: Unique identifier
    create_timestamp: Creation timestamp
    create_time: Creation time (structured DateTime)
    update_timestamp: Update timestamp
    update_time: Update time (structured DateTime)
    is_deleted: Soft delete flag
    status: Status field
    """

    hidden_fields = []  # Fields to be excluded from response
    handle_property = False  # Whether to call gen_property_fields()

    __abstract__ = True

    id = db.Column(BIGINT(20, unsigned=True), primary_key=True, autoincrement=True, comment='ID')
    create_time = db.Column(db.DateTime, server_default=db.func.now(), comment='Creation time (structured DateTime)')
    create_timestamp = db.Column(BIGINT(20, unsigned=True), default=int(time.time()), comment='Creation time (timestamp)')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='Update time (structured DateTime)')
    update_timestamp = db.Column(BIGINT(20, unsigned=True), onupdate=int(time.time()), comment='Update time (timestamp)')
    is_deleted = db.Column(BIGINT(20, unsigned=True), default=0, comment='0: Active; Other: Deleted')
    status = db.Column(TINYINT(1, unsigned=True), server_default=text('1'), comment='Status')

    def __getitem__(self, item):
        return getattr(self, item)

    def get_columns(self):
        """Return all column objects"""
        return self.__table__.columns

    def get_fields(self):
        """Return all fields"""
        return self.__dict__

    def gen_property_fields(self):
        """Process @property fields so they are included in to_json() output"""
        d = {name: self.__getattribute__(name) for name, obj in vars(self.__class__).items() if isinstance(obj, property)}
        return d

    @staticmethod
    def var_format(field):
        """Format field types to prevent JSON serialization errors"""
        if not field:
            return field
        elif isinstance(field, decimal.Decimal):  # Decimal -> float
            field = round(float(field), 2)
        elif isinstance(field, datetime):  # datetime -> str
            field = str(field)
        return field

    def to_json(self, hidden_fields=None):
        """
        Serialize model to JSON format
        :param hidden_fields: Override class-level hidden_fields
        """
        hf = hidden_fields if hidden_fields and isinstance(hidden_fields, list) else self.hidden_fields
        model_json = {}
        for column in self.get_fields():
            if column not in hf:
                if hasattr(self, column):
                    field = getattr(self, column)
                    model_json[column] = self.var_format(field=field)
        del model_json['_sa_instance_state']
        if self.handle_property:
            property_dict = self.gen_property_fields()
            if property_dict:
                for key, var in property_dict.items():
                    property_dict[key] = self.var_format(field=var)
            model_json.update(property_dict)
        return model_json

    def save(self):
        """Insert record into the database"""
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException as e:
            db.session.rollback()
            raise TypeError('Save error {}'.format(str(e)))

    @staticmethod
    def save_all(model_list):
        """Batch insert records"""
        try:
            db.session.add_all(model_list)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise TypeError('Save_all error {}'.format(str(e)))

    def delete(self):
        """Soft delete record"""
        try:
            self.is_deleted = self.id
            db.session.commit()
        except BaseException as e:
            db.session.rollback()
            raise TypeError('Delete error {}'.format(str(e)))
