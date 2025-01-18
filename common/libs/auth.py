# -*- coding: utf-8 -*-
# @Time    : 2024/01/18 4:02 PM
# @Author  : Pedro Anisio Silva
# @Email   : pedroanisio@arc4d3.com
# @File    : auth.py
# @Software: PyCharm

import json
import uuid

from config.config import config_obj

"""
Test:

import redis

redis_obj = {
    'host': 'localhost',
    'port': 6379,
    'password': 123456,
    'decode_responses': True,
    'db': 10
}
POOL = redis.ConnectionPool(**redis_obj)
R = redis.Redis(connection_pool=POOL)

"""

R = config_obj['new'].R


class Token:
    """
    Token Management
    """

    def __init__(self):
        self.token = None
        self.mix = "Y"
        self.timeout = 3600 * 24 * 30

    def gen_token(self):
        """
        Generate a token
        """
        token = str(uuid.uuid1()).replace('-', self.mix)
        self.token = token
        return token

    def set_token(self, user_info: dict):
        """
        Cache the token
        
        :param user_info: User information dictionary
        """

        self.gen_token()
        user_id = user_info.get('id')
        username = user_info.get('username')
        token_key = f"user:{user_id}-{username}"
        user_key = f"token:{self.token}"
        R.hset(name=token_key, mapping={"token": self.token})
        R.hset(name=user_key, mapping={"user_info": json.dumps(user_info, ensure_ascii=False)})
        R.expire(token_key, self.timeout)
        R.expire(user_key, self.timeout)

    @classmethod
    def del_cache(cls, token):
        """
        Delete cached token
        
        :param token: Token string
        """

        user_key = f"token:{token}"
        query_user_info = R.hget(user_key, 'user_info')
        if query_user_info:
            user_info = json.loads(query_user_info)
            user_id = user_info.get('id')
            username = user_info.get('username')
            token_key = f"user:{user_id}-{username}"
            R.delete(user_key)
            R.delete(token_key)

    def refresh_cache(self, user_info: dict):
        """
        Refresh cached token
        
        :param user_info: User information dictionary
        """

        user_id = user_info.get('id')
        username = user_info.get('username')
        token_key = f'user:{user_id}-{username}'
        old_token = R.hget(token_key, 'token')
        if old_token:
            self.del_cache(token=old_token)  # Delete old token

        self.set_token(user_info=user_info)  # Generate new token and store in Redis

    @staticmethod
    def get_user_info(token):
        """
        Retrieve user information from a token
        
        :param token: Token string
        :return: User information dictionary or None
        """
        
        query_token = R.hget(f"token:{token}", 'user_info')
        if query_token:
            return json.loads(query_token)
        return None


if __name__ == '__main__':
    t = Token()
    d = {
        "id": 1,
        "is_deleted": 0,
        "code": "00001",
        "status": 1,
        "login_type": None,
        "username": "admin",
        "creator": "shell",
        "create_time": "2021-11-11 11:15:29",
        "nickname": "yyx",
        "creator_id": 0,
        "modifier": "admin",
        "create_timestamp": 1636600147,
        "phone": "15011111111",
        "modifier_id": 1,
        "update_time": "2022-08-17 17:53:07",
        "mail": "yang6333yyx@126.com",
        "remark": "Guest",
        "update_timestamp": 1660729764
    }
    t.refresh_cache(user_info=d)
    print(t.token)
    user_info = t.get_user_info(token=t.token)
    print(user_info)
