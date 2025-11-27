# 调查用户想去度假的地方
vacation_place = {}

# 开始循环
while True:

    # 提示客户输入自己的姓名
    customer_name = input('你好,请输入你的姓名:\n')

    # 检查用户的输入
    # 如果输入quit 则立即退出程序
    if customer_name == 'quit':
        print('你选择退出程序,现在结束')
        break
    # 不能输入非字符内容,否则提示客户重新输入
    if customer_name.isdigit():
        print('您的输入有误,请重新输入')
        continue

    # 让用户输入想去的地方
    place = input('请输入你旅游最想去的地方')

    # 如果输入quit 则立即退出程序
    if place == 'quit':
        print('你选择退出程序,现在结束')
        break
    # 不能输入非字符内容,否则提示客户重新输入
    if place.isdigit():
        print('您的输入有误,请重新输入')
        continue

    vacation_place[customer_name] = place

print('-------------调查结果如下-------------')
for name,city in vacation_place.items():
    print(f'{name}最想去旅游的城市是{city}')
