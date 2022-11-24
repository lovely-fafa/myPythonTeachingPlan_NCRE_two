# day04

# jieba 库

## 01 分词

基于字典的分词。

```python
jieba.lcut(s)

Building prefix dict from the default dictionary ...
Dumping model to file cache C:\Users\lenovo\AppData\Local\Temp\jieba.cache
Loading model cost 0.686 seconds.
Prefix dict has been built successfully.
['果然', '到', '了', '一定', '的', '年纪', '就', '会', '有', '特定', '的', '烦恼', '。', '别的', '女孩子', '都', '把', '自己', '的', '彩礼', '想', '好', '了', '，', '我', '连', '结婚', '这些', '事', '什么', '都', '不', '了解', '。', '最', '重要', '的', '是', '连', '对象', '都', '没有', '。', '一天天', '的', '跟', '个', '傻子', '一样', '乐呵呵', '的', '。']
```

## 02 统计词频

- 字典取值

  ```python
  count_dict = {}
  count_dict['乐呵呵'] = 0
  count_dict
  {'乐呵呵': 0}
  count_dict['乐呵呵']
  0
  count_dict['乐 呵呵']
  Traceback (most recent call last):
    File "<pyshell#10>", line 1, in <module>
      count_dict['乐 呵呵']
  KeyError: '乐 呵呵'
  count_dict.get('乐呵呵')
  0
  count_dict.get('乐呵呵', '没有这个东西')
  0
  count_dict.get('乐 呵呵', '没有这个东西')
  '没有这个东西'
  ```

- 字典的知识点

  ```python
  # 取键
  dic.keys()
  
  # 取值
  dic.values()
  
  # 同时取
  dic.items()
  
  
  for i, j in res.items():
      # print(i)  # 这个 i 是建
      # print(res[i])  # 取值 不推荐
      print(i, j)
  ```

- 字典排序

  ```python
  res = {'果然': 6, '到': 1, '了': 2, '一定': 1, '年纪': 1, '就': 1, '会': 1, '有': 1, '特定': 1, '烦恼': 1, '别的': 1, '女孩子': 1, '都': 3, '把': 1, '自己': 1, '彩礼': 1, '想': 1, '好': 1, '，': 1, '我': 1, '连': 2, '结婚': 1, '这些': 1, '事': 1, '什么': 1, '不': 1, '了解': 1, '最': 1, '重要': 1, '是': 1, '对象': 1, '没有': 1, '一天天': 1, '跟': 1, '个': 1, '傻子': 1, '一样': 1, '乐呵呵': 1}
  
  # for i in res.items():
  #     # print(i)  # 这个 i 是建
  #     # print(res[i])  # 取值 不推荐
  #     print(i)
  
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
  ```

- 整个过程

  ```python
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
  ```

  





