# 修改属性的值
# 直接修改属性的值
class Car():

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.color = '红色'

    def describe_car(self):
        print(f'{self.brand} {self.model} {self.color}')

    # 通过方法修改属性的值
    def update_color(self,color):
        self.color = color

my_car = Car('奥迪','RS7')
# 这里直接修改
my_car.color = '黑色'
my_car.describe_car()
# 调用方法来修改颜色
my_car.update_color('白色')
my_car.describe_car()