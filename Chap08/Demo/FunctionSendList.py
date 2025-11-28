# 向列表中每个用户问好
def say_hello(names):
    for name in names:
        message = f'你好 {name}'
        print(message)

usernames = ['张三','李四','王五']
say_hello(usernames)
