#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-11-17 16:44
# @Author  : 发发
# @QQ      : 1315337973
# @File    : 1.py
# @Software: PyCharm

import missingno
from sklearn.ensemble import RandomForestRegressor

missingno.bar()
fit = RandomForestRegressor()
fit.fit()
