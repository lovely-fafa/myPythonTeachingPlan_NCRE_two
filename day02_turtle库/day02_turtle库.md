- 第一节课有一个地方讲错了？
- 从华为，小米 OPPO 

random.choice([华为,小米 ,OPPO ])

```[华为,小米 ,OPPO ][random.randint(0, 4)]```



# 今天的 turtle 库

> https://www.zhihu.com/search?type=content&q=turtle%E5%BA%93

## 导入

```python
import turtel
import turtel as t
```

# 两种状态

- 在沙滩上

  ```t.down()```或```t.pendown()```

  移动就会留下轨迹

- 飞起来了

  ```t.up()```或```t.penup()```

  移动就不会留下轨迹

# 两套移动系统

- 第一种

  > 相对状态

  - 往前走

    ```forward(distance)```或```fd(distance)```

  - 转向

    ```left(angle)```

    ```right(angle)```

- 第二种

  > 绝对状态

  - 去往某个地方

    ```goto(x, y)```

  - 旋转到什么方向

    ```seth(to_angle)```
    
    