# 组合
class Flavors:

    def __init__(self,flavor_list):
        self.flavor_list = flavor_list

    def describe_flavors(self):
        print(f'主要口味有{self.flavor_list}')

# 父类
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'餐厅名称是{self.name},主要是做{self.cuisine_type}的')

    def open_restaurant(self):
        print(f"{self.name}现在是正常营业的")

# 子类 冰淇淋店铺
class Ice_Cream_Store(Restaurant):

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def describe_ice_cream_store(self):
        print(f'这家餐厅的名称是{self.name},主要是做{self.cuisine_type}的,主要口味有{self.flavors.flavor_list}')

Ice_World_Flavors = Flavors(['草莓','芒果','西瓜'])
Ice_World = Ice_Cream_Store('冰雪世界','冰淇淋',Ice_World_Flavors)
Ice_World.describe_ice_cream_store()