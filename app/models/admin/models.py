# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 9:44 AM
# @Author  : ShaHeTop-Almighty-ares
# @Email   : yang6333yyx@126.com
# @File    : models.py
# @Software: PyCharm

from werkzeug.security import generate_password_hash, check_password_hash

from common.libs.BaseModel import *

"""
RBAC
User - Role - Permission
"""

crm_user_and_role = db.Table(
    'cms_user_and_role',
    db.Column('cms_user_id', BIGINT(20, unsigned=True), db.ForeignKey('crm_user.id'), primary_key=True, comment='User ID'),
    db.Column('cms_role_id', BIGINT(20, unsigned=True), db.ForeignKey('crm_role.id'), primary_key=True, comment='Role ID'),
    comment='User_Role_Mapping_Table'
)

crm_permission_and_role = db.Table(
    'cms_permission_and_role',
    db.Column('cms_permission_id', BIGINT(20, unsigned=True), db.ForeignKey('crm_permission.id'), primary_key=True, comment='Permission ID'),
    db.Column('cms_role_id', BIGINT(20, unsigned=True), db.ForeignKey('crm_role.id'), primary_key=True, comment='Role ID'),
    comment='Permission_Role_Mapping_Table'
)


class Admin(BaseModel):
    __tablename__ = 'crm_user'
    __table_args__ = {'comment': 'Admin User Table'}
    username = db.Column(db.String(50), nullable=False, comment='Username')
    _password = db.Column(db.String(100), nullable=False, comment='Password')
    mail = db.Column(db.String(100), nullable=True, comment='Email')
    remark = db.Column(db.String(255), nullable=True, comment='Remarks')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result

    def get_role(self):
        """Get all roles of the current user"""
        roles = self.roles
        roles_json = [r.to_json() for r in roles]
        return roles_json

    def get_permission(self):
        """Get all permissions of the current user"""
        roles = self.roles
        permission_set = []
        for r in roles:
            permission_set += r.permission_list
        permission_json = [p.to_json() for p in list(set(permission_set))]
        return permission_json

    def __repr__(self):
        return 'Admin Model Object-> ID:{} Username:{}'.format(self.id, self.username)


class Role(BaseModel):
    __tablename__ = 'crm_role'
    __table_args__ = {'comment': 'Admin Role Table'}
    name = db.Column(db.String(50), nullable=False, comment='Role Name')
    remark = db.Column(db.String(255), nullable=True, comment='Remarks')

    user_list = db.relationship('Admin', secondary=crm_user_and_role, backref='roles')
    permission_list = db.relationship('Permission', secondary=crm_permission_and_role, backref='roles')

    def __repr__(self):
        return 'Role Model Object-> ID:{} Role Name:{}'.format(self.id, self.name)


class Permission(BaseModel):
    __tablename__ = 'crm_permission'
    __table_args__ = {'comment': 'Admin Permission Table'}
    name = db.Column(db.String(50), nullable=False, comment='Permission Name')
    remark = db.Column(db.String(255), nullable=True, comment='Remarks')

    def __repr__(self):
        return 'Permission Model Object-> ID:{} Permission Name:{}'.format(self.id, self.name)
