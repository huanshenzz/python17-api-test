#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: variable
# Author: 郑
# Time: 2019/5/31
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 根目录
cases_file = os.path.join(base_dir, "data", "cases.xlsx")

test_file = os.path.join(base_dir, "data", "my_conf.conf")

logs_file = os.path.join(base_dir, "logs", "api.log")

testcases_dir = os.path.join(base_dir, "testcases")

repprt_file = os.path.join(base_dir, "report","api.html")
