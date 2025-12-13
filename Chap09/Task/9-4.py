class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # 新增属性，记录就餐人数，
    
    def describe_restaurant(self):
        print(f'餐馆的名称是{self.restaurant_name},餐馆的类型是{self.cuisine_type},有{self.number_served}位顾客就餐过')
    
    def set_number_served(self,number):
        self.number_served = number  # 方法，用于设置就餐人数

    def increment_number_served(self,increment):
        self.number_served += increment  # 方法，用于递增就餐人数

KFC = Restaurant('肯德基','快餐')

KFC.describe_restaurant()

KFC.number_served = 20  # 来过20位顾客
KFC.describe_restaurant()

KFC.set_number_served(35)   # 来过35位客户
KFC.describe_restaurant()

KFC.increment_number_served(15)  # 又来过15位客户 是基于上次的35位加上的
KFC.describe_restaurant()