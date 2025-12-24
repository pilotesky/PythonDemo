class User:

    # 初始化属性
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts 
    # 打招呼
    def greet_user(self):
        full_name = self.first_name + self.last_name
        print(f'你好 {full_name}')

    # 信息摘要
    def describe_user(self):
        print(f'这位用户的姓名是{self.first_name}{self.last_name}')

    # 说明登录次数
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    # 将登录次数重置为0
    def reset_login_attempts(self):
        self.login_attempts = 0

xiaomi = User('小','米')
xiaomi.describe_user()
xiaomi.increment_login_attempts()
xiaomi.increment_login_attempts()
xiaomi.increment_login_attempts()
print(f'当前总计的登录次数有{xiaomi.login_attempts}')

xiaomi.reset_login_attempts()
print(f'重置后的登录次数为{xiaomi.login_attempts}')

jason = User('杰','森')
jason.describe_user()
jason.increment_login_attempts()
jason.increment_login_attempts()
jason.increment_login_attempts()
print(f'当前总计的登录次数有{jason.login_attempts}')
jason.reset_login_attempts()
print(f'重置后的登录次数为{jason.login_attempts}')
