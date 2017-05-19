# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from core import create_role_url


# Create your tests here.
class UserTest(TestCase):

    def test_insert_role_url(self):
        data_list = [
            {'url_id': 1, 'url_parent_id': -1, 'url': 'www.hao123.com', 'url_name': '系统导航', 'url_icon': 'icon_save'},
            {'url_id': 2, 'url_parent_id': 1, 'url': 'www.hao123.com', 'url_name': '用户管理', 'url_icon': 'icon_save'},
            {'url_id': 21, 'url_parent_id': 2, 'url': 'www.hao123.com', 'url_name': '用户列表', 'url_icon': 'icon_save'},
            {'url_id': 3, 'url_parent_id': 1, 'url': 'www.hao123.com', 'url_name': '考勤管理', 'url_icon': 'icon_save'},
            {'url_id': 31, 'url_parent_id': 3, 'url': 'www.hao123.com', 'url_name': '考勤记录', 'url_icon': 'icon_save'},
            {'url_id': 32, 'url_parent_id': 3, 'url': 'www.hao123.com', 'url_name': '办公申请', 'url_icon': 'icon_save'},
            {'url_id': 4, 'url_parent_id': 1, 'url': 'www.hao123.com', 'url_name': '邮件管理', 'url_icon': 'icon_save'},
            {'url_id': 41, 'url_parent_id': 4, 'url': 'www.hao123.com', 'url_name': '收件箱', 'url_icon': 'icon_save'},
            {'url_id': 42, 'url_parent_id': 4, 'url': 'www.hao123.com', 'url_name': '发件箱', 'url_icon': 'icon_save'},
            {'url_id': 5, 'url_parent_id': 1, 'url': 'www.hao123.com', 'url_name': '公告管理', 'url_icon': 'icon_save'},
            {'url_id': 51, 'url_parent_id': 5, 'url': 'www.hao123.com', 'url_name': '公告列表', 'url_icon': 'icon_save'}
        ]
        for data in data_list:
            create_role_url(url_id=data.get('url_id'), url_parent_id=data.get('url_parent_id'),
                            url=data.get('url'), url_name=data.get('url_name'), url_icon=data.get('url_icon')
                            )

