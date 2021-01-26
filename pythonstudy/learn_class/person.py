#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : person.py
# @Author: wzz
# @Date  : 2021-01-22
# @Desc  :
"""
创建一个Person类：属性：姓名、性别、年龄、存款金额；方法：吃，睡，跑，赚钱
创建 FunnyMan类（喜剧演员）：继承父类Person的所有属性和方法，新增方法：搞笑
创建 SingerMan类（歌手）：继承父类Person的所有属性和方法，覆写方法：赚钱
"""

class Person:
    name:str = "default"
    gender:str = "default"
    age:int = 25
    money:int = 1000
    __money = 2000
    def __init__(self,name):
        # print("init")
        self.name=name
    def eat(self):
        print("eating")
    def sleep(self):
        print("sleep")
    def __run(self):
        print("run")
    def make_money(self):
        print(f"{self.name} make money:{self.money}")
        print(f"{self.name} have money:{self.__money}")


class Funny_Man(Person):
    pass

class Singer_Man(Person):
    def make_money(self,moneynum):
        print(f"{self.name} have money:{moneynum}")
    def write_song(self):
        print(f"{self.name} is writing songs")

# p = Person("aaa")
# print(f"name: {p.name}")

funnyman=Funny_Man("bbb")
# print(funnyman.name)
funnyman.make_money()
# print(funnyman.money)
# print(dir(p))
# funnyman._Person__run()

singer=Singer_Man("ccc")
singer.make_money(222)
singer.write_song()