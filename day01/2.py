#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-11-16 20:10
# @Author  : 发发
# @QQ      : 1315337973
# @File    : 2.py
# @Software: PyCharm
a, b = 0, 1
while a < 100:
    print(a, end=',')
    a, b = a + b, a
