#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: logger
# Author: 郑
# Time: 2019/6/12

import  logging
from logging.handlers import  RotatingFileHandler
from python17.port_test.common import  variable

class Logger:
    def __init__(self,name):
        self.log = logging.getLogger(name)
        self.log.setLevel('DEBUG')   # 总开关

        # 设置日志输出格式
        fmt ='%(asctime)s-%(levelname)s-%(message)s[ %(lineno)d : %(filename)s]'
        formatter = logging.Formatter(fmt)

        # 输出的渠道
        consur_handle = logging.StreamHandler()  # 选择输出位置--控制台
        consur_handle.setLevel('DEBUG')
        consur_handle.setFormatter(formatter)

        file_handle = RotatingFileHandler(variable.logs_file,maxBytes=1024*1024,
                                          backupCount=10,encoding='utf-8')    # 选择输出位置--文件

        # 文件位置  每一个log文件最大字节大小  文件个数  编码格式
        file_handle.setLevel('INFO')
        file_handle.setFormatter(formatter)

        # 把添加的handle输出   添加到实例中
        self.log.addHandler(consur_handle)
        self.log.addHandler(file_handle)

    def info(self, msg):
        self.log.info(msg)

    def debug(self, msg):
        self.log.debug(msg)

    def error(self, msg):
        self.log.error(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def critical(self, msg):
        self.log.critical(msg)

log = Logger('api')


