# 位置形参

# 定义一个函数 内容是我的相关信息,包括姓名 年龄 工资 这里三个参数都是形参
def describe_myinfo(name,age,job):
    # 函数的作用是输出一段自我介绍
    print(f'大家好,我叫{name},今年{age}岁,从事{job}方面的工作')

# 调用函数 多次调用 将相关具体信息带入进去然后输出出来
describe_myinfo('陈卓伟',27,'IT运维')
describe_myinfo('徐红豆',22,'大堂经理')
# 顺序要对,否则输出的不对,下面是错误demo
describe_myinfo(30,'张三','调酒师')