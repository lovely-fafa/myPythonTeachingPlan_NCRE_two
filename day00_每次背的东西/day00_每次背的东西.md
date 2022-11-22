# 每日一背

## 1 库的安装等

> 库 模块
>
> 1、自带 turtle os math
>
> 2、第三方库、第三方模块 matplotlib jieba
>
> 3、当然你可以import自己写的

- 安装工具

  ```pip```

- 使用方法

  - 正常方法

    ```pip install 库名```

  - 删除库

    ```pip uninstall 库名```

  - 镜像网站

    ```pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple```

  - 升级库

    
  
  - 升级```pip```
  
    ```python -m pip install --upgrade pip```

## 导入库

- 最简单

  ```python
  # 有一个 import
  # as 是别名的意思 可有可无
  # from import as 按照这个顺序
  import matplotlib
  from matplotlib.pyplot import plot
  from matplotlib import pyplot
  # 这个不推荐
  from math import *
  ```

## 2 要背的库

### 2.1 数据分析

> 数据分析的三剑客

- ```pandas```

  表单数据处理

- ```matplotlib```

  科学绘图

- ```numpy```

  矩阵计算

### 2.2 网络爬虫

- ```urllib3```
- ```requests```
- ```scrapy```

### 2.3 办公自动化

- ```openpyxl```或```openPyXl```

  处理Excel文件

- ```python-docx```

  处理Word文档

### 2.4 界面

- ```pyqt5```
- 



### 2.5 深度学习、机器学习、强化学习、人工智能

- ```sklearn```或```scikit-learn```
- ```PyTorch```

### 2.6 把```python```封装成 exe 文件 / 可执行文件

- ```pyinstaller```



### 2.7 做游戏

- ```pygame```





## 3 要背的函数

- ```chr()```
- ```ord()```