#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: get_url
# Author: 郑
# Time: 2019/6/3
import configparser

from python17.port_test.common.variable import test_file


class ConfigHandler:

    def __init__(self):
        self.config = configparser.ConfigParser()  # 实例化对象
        self.config.read(test_file, encoding='utf-8')  # 先加载配置文件

handler = ConfigHandler()