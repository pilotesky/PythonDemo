# 一个基础的function demo

# 定义一个函数 名称是say_hello
def say_hello():
    # 函数的用处是输出 你好 这一段话
    print('你好')

# 调用函数
say_hello()

# 给函数里面传参 本例中函数名称是say_hey,传递了一个name的形参
def say_hey(name):
    # 函数的作用是 输出一段话 hello 加上 name这个形参对应的实参
    print(f'hello {name}')
# 调用函数并传递一个实参,这里 大爷 就是实参
say_hey('大爷')
