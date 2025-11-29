# 定义了一个名为Dog的类
class Dog():

    def __init__(self,name,age):
        # 初始化属性name和age
        self.name = name
        self.age = age

    def sit(self):
        # 让其坐下
        print(self.name.title() + '现在是坐下的')

    def roll(self):
        # 让其打滚
        print(self.name.title() + '现在是打滚的')

# 创建对应的第一个对象实现
my_dog = Dog('captain',2)
# 调取属性
print(f'我家狗子昵称是{my_dog.name}')
print(f'我家狗子今年已经{my_dog.age}岁')
# 调用函数
my_dog.sit()
my_dog.roll()

# 创建对应的第二个对象实现
friend_dog = Dog('pilote',3)
# 调取属性
print(f'朋友的狗子昵称是{friend_dog.name}')
print(f'朋友的狗子今年{str(friend_dog.age)}岁')
# 调用函数
friend_dog.sit()
friend_dog.roll()