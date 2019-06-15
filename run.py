#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: run
# Author: 郑
# Time: 2019/6/12

import unittest
from python17.port_test.common import variable,HTMLTestRunnerNew

discover = unittest.defaultTestLoader.discover(variable.testcases_dir,"test_*.py")
with open(variable.repprt_file, "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="Python17-api-test",
                                              description="前程贷",
                                              tester="幻神")
    runner.run(discover)