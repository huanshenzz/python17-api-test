#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_20190528
# Author: 郑
# Time: 2019/5/30

import  unittest
# 1  套件实例化
s = unittest.TestSuite()
# 2 收集器实例化，收集用例的方式： discover方式
t = unittest.TestLoader()
# 3  将收集到的用例，放到测试套件当中。
s.addTests(t.discover(r"D:\pycharm-workplace\python17\class_20190528\class_20190528\testcases"))
# 4、生成html测试报告  HtmlTestRunner()
from HTMLTestRunnerNew import HTMLTestRunner
# 打开一个html文件
fs = open("my_test_report.html","wb")
# 实例化html结果的用例运行器
runner = HTMLTestRunner(fs,title="前程贷测试用例",description="20190528作业测试用例",tester="幻神")
# 运行测试套件
runner.run(s)