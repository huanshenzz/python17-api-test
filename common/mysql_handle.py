#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: mysql
# Author: 郑
# Time: 2019/6/7

import pymysql

from  python17.port_test.common.get_conf_data import handler

class Mysql:

    def __init__(self):
        # 1，通过客户端进行连接  ip:port/域名  用户名&密码
        self.mysql = pymysql.Connect(host=handler.config.get('db', 'host'), user=handler.config.get('db', 'usr'),
                                     password=handler.config.get('db', 'pwd'), charset='utf8', autocommit=True,
                                     port=handler.config.getint('db', 'port'))
        # host  user pwd  必传  charset 编码  不能utf-8  autocomit自动提交（最好传True） port 端口号 默认不对的话就传
        # 2. 建立游标，保存查询结果
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 建立游标，保存查询结果

    def query_one(self, sql):
        self.cursor.execute(sql)
        return  self.cursor.fetchone()
    
    def query_all(self,sql):
        self.cursor.execute(sql)
        return  self.cursor.fetchall()

    def close_all(self):
        self.cursor.close()
        self.mysql.close()
