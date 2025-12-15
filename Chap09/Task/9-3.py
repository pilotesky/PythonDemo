class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"用户的名字是：{self.first_name} {self.last_name}，年龄是：{self.age}岁。")

    def greet_user(self):
        print(f"欢迎您，{self.first_name} {self.last_name}！")

# 测试
zhangsan = User('张', '三', 20)
zhangsan.describe_user()
zhangsan.greet_user()

xiaomi = User('小', '米', 18)
xiaomi.describe_user()
xiaomi.greet_user()

lisi = User('李', '四', 22)
lisi.describe_user()
lisi.greet_user()