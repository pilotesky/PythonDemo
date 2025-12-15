class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'餐厅名称是{self.name},主要是做{self.cuisine_type}的')

    def open_restaurant(self):
        print(f"{self.name}现在是正常营业的")

KFC = Restaurant('肯德基', '西式快餐')
KFC.describe_restaurant()
KFC.open_restaurant()

Shaxian = Restaurant('沙县小吃', '中式快餐')
Shaxian.describe_restaurant()
Shaxian.open_restaurant()

Green_Tea = Restaurant('绿茶餐厅', '中式正餐')
Green_Tea.describe_restaurant()
Green_Tea.open_restaurant()


