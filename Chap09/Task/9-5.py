class User():

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.login_attempts = 0  # 新增属性，记录登录次数，初始值为0
    
    def increment_login_attempts(self):
        self.login_attempts += 1  # 方法，用于递增登录次数
    
    def reset_login_attempts(self):
        self.login_attempts = 0  # 方法，用于重置登录次数

xiaomi = User('小米',18)

xiaomi.increment_login_attempts()
print(f'{xiaomi.name}登录了{xiaomi.login_attempts}次')
xiaomi.reset_login_attempts()
print(f'{xiaomi.name}登录了{xiaomi.login_attempts}次')
