class User:

    # 初始化属性
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def greet_user(self):
        full_name = self.first_name + self.last_name
        print(f'你好 {full_name}')

    # 信息摘要
    def describe_user(self):
        print(f'这位用户的姓名是{self.first_name}{self.last_name}')

# 根据类创建实例
my_info = User('陈','卓伟')
my_info.describe_user()
my_info.greet_user()

friend_info = User('张','三')
friend_info.describe_user()
friend_info.greet_user()

neighborhood_info = User('李','四')
neighborhood_info.describe_user()
neighborhood_info.greet_user()