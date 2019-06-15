#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_invest
# Author: 郑
# Time: 2019/6/10

import  unittest
from python17.port_test.common import  my_excel1,variable,http_my_requests,mysql_handle,context
from python17.port_test.common.logger import log
from ddt import ddt,data

cookies = None
@ddt
class TestLogin(unittest.TestCase):
    execl = my_excel1.ExcelV2(variable.cases_file, 'invest')
    cases = execl.read_excel()

    @classmethod
    def setUpClass(cls):
        cls.mysql = mysql_handle.Mysql()
    def setUp(self):
        print("开始一条用例测试")
    def tearDown(self):
        print("一条用例执行完成")

    @data(*cases)
    def test_invest_1(self,case):
        global cookies
        log.info("全局cookies{}".format(cookies))
        # 完成参数化  调用replace方法  把data替换后重新赋值给data  做后续的操作
        case['data']  = context.Context.replace(case['data'])
        data = eval(case['data'])   # str to dict
        log.info("********************")
        log.info("正在执行第{}条测试用例，标题是{}".format(case["case_id"],case["title"]))

        res = http_my_requests.HttpRequest(case["method"],case['url'],data= data,cookies=cookies)
        try:
            self.assertEqual(str(case['expected']),res.get_json()['code'])
            self.execl.write_result(case['case_id']+1,res.get_text(),'PASS')
            if res.get_json()['msg']== '加标成功':
                sql = 'SELECT * FROM future.loan WHERE MemberID = {} order by CreateTime desc limit 1'\
                    .format(data['memberId'])
                load_id  = self.mysql.query_one(sql)['Id']
                log.info("标的id".format(load_id))
                setattr(context.Context,'load_id',str(load_id))   # 这里把取到的load_id转换为str  待会替换不会报错
                #  把上下文类中load_id设置成sql查询到的load_id 反射到上下文中
            if res.get_cookies():  # 判断响应里面有cookies，我就存放
                cookies = res.get_cookies()  # 存放cookies

        except AssertionError as a:
            self.execl.write_result(case['case_id'] + 1, res.get_text(), 'FAIL')
            log.warning("断言失败")
            raise a