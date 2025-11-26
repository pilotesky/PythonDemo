# 下单的菜品订单
food_orders = ['热干面','三鲜豆皮','黑鱼面','热干面','热干面','莲藕排骨汤']

# 先说明热干面买完了
print('热干面卖完了')

while '热干面' in food_orders:
    food_orders.remove('热干面')
print(f'实际出餐的订单菜品是:{food_orders}')