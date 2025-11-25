message = '请输入您的年龄,我将自动计算您所需支付的票价金额\n'

while True:
    age = input(message)
    if int(age) > 0 and int(age) <= 3:
        print('小朋友恭喜你，免票')
    elif int(age) >3 and int(age) <= 12:
        print('你好,本次观影需要支付10美元')
    elif int(age) > 12:
        print('你好,本次观影需要支付15美元')
    else:
        print('您的输入有误,程序结束')
        break