#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_case1
# Author: 郑
# Time: 2019/5/31

import  unittest
from python17.port_test.common import  my_excel1,variable,http_my_requests,mysql_handle
from ddt import ddt,data
from python17.port_test.common.logger import log
cookies = None
@ddt
class TestRegister(unittest.TestCase):
    execl = my_excel1.ExcelV2(variable.cases_file, 'register')
    cases = execl.read_excel()

    @classmethod
    def setUpClass(cls):
        cls.mysql = mysql_handle.Mysql()
    def setUp(self):
        print("开始一条用例测试")
    def tearDown(self):
        print("一条用例执行完成")
    @data(*cases)
    def test_register_1(self,case):
        global cookies
        log.debug("全局cookies{}".format(cookies))
        if case['data'].find('register_phone') > -1:
            sql = "select max(mobilephone) as maxphone from future.member where mobilephone like '136%'"
            result = self.mysql.query_one(sql=sql)
            log.debug("最大手机号是：{}".format(result['maxphone']))
            max_phone = int(result['maxphone']) + 1000
            case['data'] = case['data'].replace('register_phone', str(max_phone))

        data = eval(case['data'])  # str to dict
        log.info("现在运行的测试用例%s"%case["title"])
        request = http_my_requests.HttpRequest(case['method'], case['url'], data=data,cookies=cookies)
        try:
            self.assertEqual(case['expected'], request.get_text())
            self.execl.write_result(case['case_id'] + 1, request.get_text(), 'PASS')
            if request.get_json()['msg'] == '注册成功':
                # 注册成功检查数据是否有新增记录
                sql = 'select * from future.member where mobilephone="{0}"'.format(max_phone)
                member = self.mysql.query_one(sql)
                self.assertIsNotNone(member)

        except AssertionError as e:
            self.execl.write_result(case['case_id'] + 1, request.get_text(), 'FAIL')
            log.warning('断言失败{}'.format(e))
            raise e


