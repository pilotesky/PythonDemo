message = '请输入你的年龄,我将自动计算您所需支付的票价'
message += '如果输入quit,程序会立即结束'

while True:

    # 让用户开始输入
    age = input(message)

    # 先检查用户输入的是否为quit,如果是的则立刻退出程序
    if age.strip() == 'quit':
        print('你选择退出,程序到此结束')
        break

    # 再检查用户输入的不能是非数值内容
    if not age.isdigit():
        print('您的输入有误,请重新输入')
        continue

    # 再检查客户输入的年龄输出对应价格
    int_age = int(age)

    if 0 <= int_age <3:
        print('小朋友,本次观影你是免票的哈')
    elif 3 <= int_age < 12:
        print('你好,本次观影你需支付10美元')
    else:
        print('你好,本次观影你需支付15美元')