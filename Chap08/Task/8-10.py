# 显示原始的列表
def show_actors(actors):
    for actor in actors:
        print(actor)
# 定义一个make_great()函数输出带the great的信息
def make_great(actors):
    for top in range(len(actors)):
        actors[top] = f'the great {actors[top]}'

# 原始的演员列表
actor_list = ['张三','李四','王五']
# 输出原始的列表
show_actors(actor_list)

# 调用一次the great
make_great(actor_list)
# 输出结果
show_actors(actor_list)