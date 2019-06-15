#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_recharge
# Author: 郑
# Time: 2019/5/31
import  unittest
from python17.port_test.common import  my_excel1,variable,http_my_requests,mysql_handle
from ddt import ddt,data
from python17.port_test.common.logger import log
cookies = None

@ddt
class TestRecharge(unittest.TestCase):
    execl = my_excel1.ExcelV2(variable.cases_file, 'recharge')
    cases = execl.read_excel()

    @classmethod
    def setUpClass(cls):
        cls.mysql = mysql_handle.Mysql()
    def setUp(self):
        print("开始一条用例测试")
    def tearDown(self):
        print("一条用例执行完成")
    @data(*cases)
    def test_recharge_1(self,case):
        data = eval(case['data'])
        global cookies
        log.info("全局cookies{}".format(cookies))
        if case['expected'].find("leaveamount") > -1:
            sql = "select * from future.member where mobilephone ={}".format(data['mobilephone'])
            result = self.mysql.query_one(sql)
            log.debug("充值前的余额{}".format(result['LeaveAmount']))
            money = str(result['LeaveAmount'] + 100)
            log.debug("期望充值后的余额{}".format(money))
            # case['expected'] = case['expected'].replace('leaveamount', money)
            data1= case['expected'].replace('leaveamount', money)
            # print(type(data1))
            # print(eval(data1),type(eval(data1)),"===========")
            # case['expected'] = float(case['expected'])
            # print(type(case['expected']),case['expected'])
        log.info("现在运行的测试用例{}".format(case["title"]))
        request = http_my_requests.HttpRequest(case['method'], case['url'], data=data,cookies=cookies)
        try:
            # self.assertEqual(case['expected'],request.get_text())
            # self.execl.write_result(case['case_id'] + 1, request.get_text(), 'PASS')
            if request.get_json()['msg'] == '充值成功':
                # 充值成功检查数据剩余金额是否正确
                sql = "select * from future.member where mobilephone ={}".format(data['mobilephone'])
                result1 = self.mysql.query_one(sql)
                amount1 =str(result1['LeaveAmount'])
                log.debug("实际充值后的余额{}".format(amount1))
                self.assertEqual(eval(data1),amount1)
                self.execl.write_result(case['case_id'] + 1, request.get_text(), 'PASS')

            if request.get_cookies():  # 判断响应里面有cookies，我就存放
                cookies = request.get_cookies()  # 存放cookies

        except AssertionError as e:
            self.execl.write_result(case['case_id'] + 1, request.get_text(), 'FAIL')
            log.warning('断言失败{}'.format(e))
            raise e
