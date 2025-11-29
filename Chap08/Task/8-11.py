# 先定义一个函数 用于输出演员列表
def show_actors(actors):
    # 使用for循环输出
    for actor in actors:
        print(actor)

# 再定义一个函数用于给用户名之前加上 the great
def make_great(actors):
    # 根据索引来修改
    for index in range(len(actors)):
        actors[index] = f'the great {actors[index]}'


# 演员列表
actor_list = ['张三','李四','王五']
# 调用 输出
show_actors(actor_list)

# 调用 the great 函数
make_great(actor_list)
# 再次调用 输出
show_actors(actor_list)


# 先定义一个函数 用于输出演员列表
def show_actors(actors):
    # 使用for循环输出
    for actor in actors:
        print(actor)

# 再定义一个函数用于给用户名之前加上 the great
# 修改 make_great，返回修改后的新列表
def make_great(actors):
    for i in range(len(actors)):
        actors[i] = f'the great {actors[i]}'
    return actors
# 原始列表
actor_list = ['张三', '李四', '王五']

# 调用时传入副本，并接收返回值
great_list = make_great(actor_list[:])

# 分别打印
show_actors(actor_list)   # 原始
show_actors(great_list)   # 带 "the great"