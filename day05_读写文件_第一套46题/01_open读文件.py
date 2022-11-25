#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-11-25 22:01
# @Author  : 发发
# @QQ      : 1315337973
# @File    : 01_open读文件.py
# @Software: PyCharm

"""
参数
file
mode='r'
encoding=None,
    一般来说是 utf-8 如果报错 gbk

参数的名字一定要带上
"""

f = open("readfile.txt", mode='r', encoding='utf-8')
content = f.read()
f.close()  # 关掉这个文件 当然这个地方是读文件 关不关无所谓
print(content)
