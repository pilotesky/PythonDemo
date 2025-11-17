# 先给出每个人喜欢的数字
favourite_number = {
    'Jason':100,
    'Ray':90,
    'Clay':95,
    'Stella':95,
    'Sonny':88
}

# 打印每个人喜欢的数字
for name,number in favourite_number.items():
    print(f'{name}最喜欢的数字是{number}')


# 询问每个人是否是真的喜欢这个数字
for name in favourite_number.keys():
    result = input(f'{name} 请问这个是你最喜欢的数字吗')
    if result.lower() == 'y':
        print('是的')
    elif result.lower() == 'n':
        print('不是的')
    else:
        print('输入有误')