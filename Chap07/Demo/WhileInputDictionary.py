# 使用用户输入来填充字典
# 本例以一个调查来举例

# 先设置一个空字典来存放报告
reports = {}

# 开始循环
while True:

    # 提示用户输入姓名
    name = input('你好,请输入你的姓名:\n')
    
    # 对用户的输入进行判断,如果输入quit 则立即退出程序
    if name.strip() == 'quit':
        print('好的现在退出程序\n')
        break
    
    # 如果输入数字则跳出这个循环,继续让用户输入
    if name.isdigit():
        print('姓名不能为数字，请重新输入！\n')
        continue

    city = input('请输入你最想去的城市:\n')

    # 对用户的输入进行判断,如果输入quit 则立即退出程序
    if city.strip() == 'quit':
        print('好的现在退出程序\n')
        break
    
    # 如果输入数字则跳出这个循环,继续让用户输入
    if city.isdigit():
        print('城市名称不能为数字，请重新输入！\n')
        continue

    # 将用户和喜欢的城市绑定到reports这个字典中
    reports[name] = city

    # 询问其他人有没有想参与调查的
    repeat = input('请问还有其他人想参与此项调查吗？请输入y/n\n')
    if repeat == 'n':
        print('没有人参与,到此结束')
        break
    else:
        continue

# 使用for循环输出
for name,city in reports.items():
    print(f'{name}最喜欢去的城市是{city}')

