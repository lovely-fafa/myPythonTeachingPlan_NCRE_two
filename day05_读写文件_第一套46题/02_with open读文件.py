#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-11-25 22:01
# @Author  : 发发
# @QQ      : 1315337973
# @File    : 02_with open读文件.py
# @Software: PyCharm

"""
参数
file
mode='r'
encoding=None,
    一般来说是 utf-8 如果报错 gbk
"""

with open("readfile.txt", mode='r', encoding='utf-8') as f:
    # 缩进
    # 执行完 下一行就退出了 这个缩进 python自动帮我们保存这个文件
    content = f.read()

print(content)
