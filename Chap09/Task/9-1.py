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

# 根据类创建实例
KFC = Restaurant('肯德基','美式快餐')
print(f'这家餐厅的名称是:{KFC.restaurant_name}')
print(f'这家餐厅主要是做{KFC.cuisine_type}')
KFC.describe_restaurant()
KFC.open_restaurant()

Laoniangjiu = Restaurant('老娘舅','中式快餐')
print(f'这家餐厅的名称是:{Laoniangjiu.restaurant_name}')
print(f'这家餐厅主要是做{Laoniangjiu.cuisine_type}')
Laoniangjiu.describe_restaurant()
Laoniangjiu.open_restaurant()

Waga = Restaurant('沃歌斯','西餐')
print(f'这家餐厅的名称是:{Waga.restaurant_name}')
print(f'这家餐厅主要是做{Waga.cuisine_type}')
Waga.describe_restaurant()
Waga.open_restaurant()