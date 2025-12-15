class Restaurant:
    
    # 初始化属性
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # 说明餐厅信息
    def describe_restaurant(self):
        print(f'餐厅名称是{self.name},主要是做{self.cuisine_type}的,今天已经接待了{self.number_served}位顾客')

    # 说明餐厅状态
    def open_restaurant(self):
        print(f"{self.name}现在是正常营业的")

    # 通过方法修改属性值
    def set_number_served(self, number):
        self.number_served = number
        print(f'已将接待顾客人数为{self.number_served}位')
    # 通过方法让属性的值增加
    def increment_number_served(self,increment):
        self.number_served += increment
        print(f'已增加接待顾客人数为{increment}位,总计接待顾客人数为{self.number_served}位')

# 创建一个实例对象
KFC = Restaurant('肯德基', '西式快餐')
KFC.describe_restaurant()

# 直接修改
KFC.number_served = 100
KFC.describe_restaurant()
# 通过方法修改属性值
KFC.set_number_served(200)
KFC.describe_restaurant()
# 通过方法让属性的值增加
KFC.increment_number_served(250)

