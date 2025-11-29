# 导入 hello 模版
import hello
# 定义用户列表
user_list = ['Jason','Clay','Stella']
# 调用hello模版的say_hello函数 进行输出
hello.say_hello(user_list)

# 导入特定的函数
from hello import say_hello

member_list = ['张三','李四','王五']
say_hello(member_list)

# 使用as给函数指定别名
from hello import say_hello as initial
vip_list = ['小王','小李','小张']
initial(vip_list)

# 使用as给模块指定别名
import hello as basic
employee_list = ['王工','李工','陈工']
basic.say_hello(employee_list)

# 导入模块中所有的函数
from hello import *
famous_people_list = ['撒贝林','李思思','董卿']
hello.say_hello(famous_people_list)