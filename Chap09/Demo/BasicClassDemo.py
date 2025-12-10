class Dog():
    
    # 初始化属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 两个函数 一个是玩耍一个是睡觉
    def play(self):
        print(f'{self.name}现在正在玩耍')

    def sleep(self):
        print(f'{self.name}现在正在睡觉')

my_dog = Dog('captain',2)
friend_dog = Dog('sky',3)

# 自我介绍
print(f'大家好 我的宠物昵称是{my_dog.name},今年已经满{my_dog.age}岁')
print(f'大家好 我的宠物昵称是{friend_dog.name},今年已满{friend_dog.age}岁')

# 调用函数
my_dog.play()
my_dog.sleep()

# 再次调用
friend_dog.play()
friend_dog.sleep()