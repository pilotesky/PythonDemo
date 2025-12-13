class User():

    # 初始化属性
    def __init__(self,first_name,last_name,age,location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    # 描述用户信息
    def describe_user(self):
        print(f'用户的姓名是{self.first_name} {self.last_name},年龄是{self.age},所在地是{self.location}')

    # 打招呼
    def greet_user(self):
        print(f'欢迎您,{self.first_name} {self.last_name}!')

# 创建多个实例对象
zhangsan = User('张','三',20,'北京')
lisi = User('李','四',22,'上海')
wangwu = User('王','五',25,'广州')

zhangsan.describe_user()
lisi.describe_user()
wangwu.describe_user()
zhangsan.greet_user()
lisi.greet_user()
wangwu.greet_user()