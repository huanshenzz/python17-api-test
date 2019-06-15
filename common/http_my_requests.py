#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: http_my_requests
# Author: 郑
# Time: 2019/5/30
from python17.port_test.common.get_conf_data import handler
import  requests
class HttpRequest:

    def __init__(self, method, url, data=None, cookies=None, headers=None):
        url = handler.config.get('url', 'pre_url') + url  # 完成拼接
        method = method.upper()  # 强制转成大写
        if method == 'POST':
            self.resp = requests.post(url=url, data=data, cookies=cookies, headers=headers)
        elif method == "GET":
            self.resp = requests.get(url=url, params=data, cookies=cookies, headers=headers)
        else:
            print('不支持该请求类型，请查看你的得请求方式是否正确！！！')

    def get_status_code(self):
        return self.resp.status_code

    def get_json(self):
        return self.resp.json()

    def get_text(self):
        return self.resp.text

    def get_cookies(self):
        return self.resp.cookies
