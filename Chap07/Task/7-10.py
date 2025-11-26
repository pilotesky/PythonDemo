# 调查用的度假想去的地方
vacation_place = {}

# 开始循环
while True:
    # 让用户输入自己的姓名
    customer_name = input('您好,请输入您的姓名,如果输入quit则立即退出程序\n')
    
    # 先排除客户输入非字符和quit来退出的两种情况
    if customer_name.lower() == 'quit':
        print('您选择退出,程序到此结束')
        break
    if customer_name.isdigit():
        print('您的输入有误,请重新输入')
        continue
        