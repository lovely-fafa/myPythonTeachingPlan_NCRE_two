#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-11-25 22:33
# @Author  : 发发
# @QQ      : 1315337973
# @File    : 05_转移字符串.py
# @Software: PyCharm

"""
\n: 换行
"""
print('床前明月光\n疑是地上霜')
# 如果在 字符串前面 加一个 r 就会变成 原生字符串
print(r'床前明月光\n疑是地上霜')

# 在 路径前面一定要加一个 r
print(r'D:\install\xhktPython\folders')

# 去掉 一个字符串开头结尾的 换行符 或 空格
print('床前明月光\n疑是地上霜\n'.strip())
# 拓展
print('床前明月光\\n疑是地上霜')
