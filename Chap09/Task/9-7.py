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

class Admin(User):

    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges if privileges is not None else []
    
    def describe_admin(self):
        print(f'{self.first_name}{self.last_name}是一名管理员,他拥有的权限如下:{self.privileges}')

Xiaomi = Admin('xiao','mi',['新增用户','删除用户','查找用户'])
Xiaomi.describe_admin()