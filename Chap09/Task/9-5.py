class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"用户的名字是：{self.first_name} {self.last_name}，年龄是：{self.age}岁。")

    def greet_user(self):
        print(f"欢迎您，{self.first_name} {self.last_name}")

    # 增加登录尝试次数
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'登录尝试次数增加到{self.login_attempts}次。')
    # 重置登录尝试次数
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'登录尝试次数已重置为{self.login_attempts}次。')

# 测试
zhangsan = User('张', '三', 20)
zhangsan.describe_user()
zhangsan.greet_user()

zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()

zhangsan.reset_login_attempts()
