#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : .py
# @Author: 
# @Date  : 2021-01-27
# @Desc  : yaml学习

import yaml
document = """
  a: 1
  b:
    c: 3
    d: 4
"""

print (yaml.safe_load(document))
#{'a': 1, 'b': {'c': 3, 'd': 4}}


dict_a={'a': 1, 'b': {'c': 3, 'd': 4}}
print (yaml.dump(dict_a))


f=open('datas.yml')
t=yaml.safe_load(f)
print(t["e"]["datetime2"])