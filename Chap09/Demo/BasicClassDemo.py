class Dog:

    # 初始化属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 介绍
    def describe_dog_info(self):
        print(f'这只狗子的名称叫{self.name},今年{self.age}岁')
    
    # 玩耍
    def playing(self):
        print(f'{self.name}正在玩耍')

    # 睡觉
    def sleeping(self):
        print(f'{self.name}正在睡觉')

# 根据类创建实例
my_dog = Dog('小米',2)
# 调用说明
my_dog.describe_dog_info()
# 调用玩耍
my_dog.playing()
# 调用睡觉
my_dog.sleeping()
