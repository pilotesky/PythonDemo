# 一个基础的class demo
class Pet():

    # 初始化属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 一个自我介绍，一个玩耍
    def descibe_pet(self):
        print(f'这个宠物的名称是{self.name},今年已经满{self.age}岁')

    def play_pet(self):
        print(f'{self.name}正在玩耍中')

# 创建多个实例对象
my_pet = Pet('Captain',2)
friend_pet = Pet('Pilote',3)

# 调用方法
my_pet.descibe_pet()
my_pet.play_pet()
friend_pet.descibe_pet()
friend_pet.play_pet()