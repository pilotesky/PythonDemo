class Restaurant:

    # 初始化属性
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    # 餐厅说明
    def describe_restaurant(self):
        print(f'这家餐厅的名称是{self.restaurant_name},主要是做{self.cuisine_type}的')

    # 说明餐厅营业状态
    def open_restaurant(self):
        print(F'{self.restaurant_name}这家餐厅目前是正常营业的')

    # 说明有多少人在此门店就餐过
    def describe_number_served(self):
        print(f'目前总计有{self.number_served}位客户在本店就餐过')

    # 使用方法修改就餐人数
    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self,number):
        self.number_served += number

KFC = Restaurant('KFC','西式快餐')
KFC.number_served = 0
KFC.describe_number_served()
# 直接重新设定新的就餐人数
KFC.number_served =100
KFC.describe_number_served()
# 使用方法设定
KFC.set_number_served(200)
KFC.describe_number_served()
# 使用方法让就餐人数增加
KFC.increment_number_served(150)
KFC.describe_number_served()