#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-11-25 22:21
# @Author  : 发发
# @QQ      : 1315337973
# @File    : 04_模式.py
# @Software: PyCharm

"""
读
    mode="r"
写（覆盖）
    mode="w"
追加
    mode="a"
"""

with open("写.txt", mode='w', encoding='utf-8') as f1:

    f1.write('123')

with open("写.txt", mode='a', encoding='utf-8') as f2:
    f2.write('345')
