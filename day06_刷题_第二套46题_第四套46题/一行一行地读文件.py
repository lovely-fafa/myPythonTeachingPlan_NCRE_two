with open('sensor.txt', mode='r', encoding='utf-8') as f:
    content = f.read()
# print(content)

# 一行一行的读
# 一般是 搭配的 open
f = open('sensor.txt', mode='r', encoding='utf-8')
for one_line in f:
    print(one_line.split(','))

    break
