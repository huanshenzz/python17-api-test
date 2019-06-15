#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_login
# Author: 郑
# Time: 2019/5/31
import  unittest
from python17.port_test.common import  my_excel1,variable,http_my_requests,mysql_handle
from ddt import ddt,data
from python17.port_test.common.logger import log
@ddt
class TestLogin(unittest.TestCase):
    execl = my_excel1.ExcelV2(variable.cases_file, 'login')
    cases = execl.read_excel()

    # @classmethod
    # def setUpClass(cls):
    #     cls.mysql = mysql_handle.Mysql()
    def setUp(self):
        print("开始一条用例测试")
    def tearDown(self):
        print("一条用例执行完成")

    @data(*cases)
    def test_login_1(self,case):
        print("********************")
        log.info("正在执行第{}条测试用例，标题是{}".format(case["case_id"],case["title"]))

        res = http_my_requests.HttpRequest(case["method"],case['url'],eval(case['data']))
        try:
            self.assertEqual(case['expected'],res.get_text())
            self.execl.write_result(case['case_id']+1,res.get_text(),'PASS')

        except AssertionError as a:
            self.execl.write_result(case['case_id'] + 1, res.get_text(), 'FAIL')
            raise a