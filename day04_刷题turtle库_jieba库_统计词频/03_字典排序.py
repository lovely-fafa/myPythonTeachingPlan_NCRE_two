res = {'果然': 6, '到': 1, '了': 2, '一定': 1, '年纪': 1, '就': 1, '会': 1, '有': 1, '特定': 1, '烦恼': 1, '别的': 1, '女孩子': 1, '都': 3, '把': 1, '自己': 1, '彩礼': 1, '想': 1, '好': 1, '，': 1, '我': 1, '连': 2, '结婚': 1, '这些': 1, '事': 1, '什么': 1, '不': 1, '了解': 1, '最': 1, '重要': 1, '是': 1, '对象': 1, '没有': 1, '一天天': 1, '跟': 1, '个': 1, '傻子': 1, '一样': 1, '乐呵呵': 1}

for i in res:
    # print(i)  # 这个 i 是建
    # print(res[i])  # 取值 不推荐
    print(i)

# def func(x):
#     return res[x]
#
#
# 排序的东西 函数 是否逆序?
# res_sort = sorted(res, key=func, reverse=True)
# 去遍历第一个参数
# 把每一次遍历到的东西 丢到 key 里面 key这个函数返回一个东西作为排序的依据
res_sort = sorted(res.items(), key=lambda x: x[1], reverse=True)
# 把一个字典，按照键 去排序
res_sort = sorted(res.items(), key=lambda x: x[0], reverse=True)
print(res_sort)
