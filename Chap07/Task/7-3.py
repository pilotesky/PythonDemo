check_num = input('请输入您想检查的数字,其是否为10的倍数\n')

if int(check_num) % 10 == 0:
    print('此数字是10的整数倍数')
else:
    print('此数字不是10的整数倍数')