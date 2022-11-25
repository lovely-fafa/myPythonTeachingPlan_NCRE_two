#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-11-25 22:14
# @Author  : 发发
# @QQ      : 1315337973
# @File    : 03_写文件.py
# @Software: PyCharm

# 写文件和读文件本质上都差不多 无非打开这个文件 然后调用 write() 写进去
# 读文件肯定要存在这个文件
# 写文件就可以没有这个文件
f = open("writefile.txt", mode='w', encoding='utf-8')
f.write('写文件')
f.close()  # 关掉这个文件 当然这个地方是读文件 关不关无所谓

# with open 写文件
with open('writefile_by_open.txt', mode='w', encoding='utf-8') as f2:
    f2.write('再写一下')

