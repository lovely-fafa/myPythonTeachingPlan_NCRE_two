import jieba
s = '果然到了一定的年纪就会有特定的烦恼。别的女孩子都把自己的彩礼想好了，我连结婚这些事什么都不了解。最重要的是连对象都没有。一天天的跟个傻子一样乐呵呵的。'
stop_words_list = ['。', '的']  # 停词表
res = jieba.lcut(s)
count_dict = {}
for i in res:
    # 停词表
    if i not in stop_words_list:
        # 统计词频
        count_dict[i] = count_dict.get(i, 0) + 1

# 字典排序
# count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=False)
count_dict = sorted(count_dict, key=lambda x: count_dict[x], reverse=False)

print(count_dict[:10])
