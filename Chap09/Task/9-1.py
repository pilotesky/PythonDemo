class Restaurant():

    # 初始化
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    # 描述餐馆信息
    def describe_restaurant(self):
        print(f'餐馆的名称是{self.restaurant_name},餐馆的类型是{self.cuisine_type}')
    
    # 显示餐馆正在营业
    def open_restaurant(self):
        print(f'{self.restaurant_name}正在营业中')

# 创建多个实例对象
KFC = Restaurant('KFC','快餐')
DQ = Restaurant('DQ','冰淇淋')
Shaxian = Restaurant('沙县小吃','中餐')

# 调用方法
KFC.describe_restaurant()
DQ.describe_restaurant()
Shaxian.describe_restaurant()
KFC.open_restaurant()
DQ.open_restaurant()
Shaxian.open_restaurant()