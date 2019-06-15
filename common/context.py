#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: context上下文管理
# Author: 郑
# Time: 2019/6/10

import re
from python17.port_test.common.get_conf_data import handler
import configparser
class Context:
    load_id  = None


    @classmethod
    def replace(cls,data):
        p = "#(.*?)#"   # 号里面是一个组  通过match对象 match.group(1)  去掉#号  取到key值 通过配置文件key取到value
        # 编译对象
        pattern = re.compile(p)
        while pattern.search(data):
            print("while循环中要替换的数据{}".format(data))
            # 拿到配置文件中key（测试data中key  同名）
            key =pattern.search(data).group(1)
            print(key)
            try:
                value = handler.config.get('data',key)
            except configparser.NoOptionError as e:
                value = getattr(Context,key)
                # 在配置文件取不到 就去测试用例中反射过来的load_id 中取  key与测试用例中load_id同名
                #  key中名字和 属性值名称一样 就可以取到多个属性值
                # 判断当前类有没有这个属性方法
                # if hasattr(Context,key):
                #     value = getattr(Context,key)

            print(value)
            # 根据配置文件的key 来替换不同的值
            data = pattern.sub(value,data,count=1)
            # TypeError: decoding to str: need a bytes-like object, int found  经常用到 代表要替换的值不是一个str  必须
            # 要求为一个str

        return data
