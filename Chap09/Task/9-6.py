# 父类
class Restaurant:

    # 初始化属性
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    # 餐厅说明
    def describe_restaurant(self):
        print(f'这家餐厅的名称是{self.restaurant_name},主要是做{self.cuisine_type}的')

    # 说明餐厅营业状态
    def open_restaurant(self):
        print(F'{self.restaurant_name}这家餐厅目前是正常营业的')

# 子类 冰淇淋店
class Ice_Cream_Store(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors if flavors is not None else []

    def describe_ice_cream_store(self):
        print(f'这家餐厅的名称是{self.restaurant_name},主要是做{self.cuisine_type},其产品主要口味有{self.flavors}')

Ice_World = Ice_Cream_Store('冰雪世界','冰淇淋',['草莓','芒果'])
Ice_World.describe_ice_cream_store()