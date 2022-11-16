# 字符串的一个方法 str.format() 代替 %
print("我叫{}，今年{}岁。".format("发发", 2))
print("我叫{}，今年{}岁。".format(3, "发发"))

# 可以看到，format函数接收的是一个元祖，故可：

num_tuple = ("发发", 3)
print("我叫{}，今年{}岁。".format(*num_tuple))
# 为什么这样不可以？

print("我叫{0}，{0}今年{1}岁。".format("发发", 3))

# 亦可使用关键词
print("我叫{name}，{name}今年{grade}年级。".format(name="发发", grade=5))

# 亦可用列表 (注意应该是“{0[0]}”，而不是“{list1[0]}”)
list1 = ["发发", 3]
list2 = ["xx", 2]
print("我是{0[0]}，今年{0[1]}！\n她是{1[0]}，今年{1[1]}岁。".format(list1, list2))


# 格式化数字(记得有:)
print("{:.5f}".format(3.14))  # 保留小数点
print("{:.0f}".format(3.14))  # 不保留
print("{:+.1f}".format(3.14))  # 带符号

# 格式化对齐
# print("{:[仅有一个填充的字符，不指定则默认是用空格][^居中/<左对齐/>右对齐][宽度][,]}".format(num))
print("{:->20,}".format(2500))

