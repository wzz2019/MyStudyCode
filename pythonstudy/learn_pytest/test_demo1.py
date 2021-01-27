#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : .py
# @Author: 
# @Date  : 2021-01-27
# @Desc  : 学习pytest
"""
命名规则：
    测试文件：test***.py
    测试类：Test***
    测试方法：test***
pycharm以pytest方式运行：
    需要改该工程设置默认的运行器，先修改，后创建测试文件
    file->Setting->Tools->Python Integrated Tools->项目名称->Default test runner->选择py.test
"""

from fun_cal import Calculator

class Testcal:
    def test_add(self):
        cal=Calculator()
        assert 3 == cal.add(1,2)

def testadd2():
    cal = Calculator()
    assert 3 == cal.add(1, 2)