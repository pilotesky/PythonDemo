# 设置默认值 年份

class Car:

    def __init__(self,brand,model,year=0):
        self.brand = brand
        self.model = model
        self.year = year

    def describe_car(self):
        print(f'这辆汽车的品牌是{self.brand},型号是{self.model},这个是{self.year}款')

    # 通过方法修改属性的值 这里以修改型号为例子
    def update_model(self,model):
        self.model = model

    # 通过方法让属性的值递增 说明明年退出的款
    def update_year(self,increment):
        self.year += increment

my_car = Car('Audi','RS7',2024)
my_car.describe_car()

# 直接修改属性的值
my_car.year = 2025
my_car.describe_car()

# 通过方法修改属性的值
my_car.model = 'A8L'
my_car.describe_car()

my_car.update_year(1)
my_car.describe_car()