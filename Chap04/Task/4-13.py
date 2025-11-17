food_list = ('手撕包菜','东坡肉','海带排骨汤','油焖大虾','剁椒鱼头')
print('本餐厅提供的菜单如下:')
for food in food_list:
    print(food)

# 尝试修改其中一道菜(失败)
# food_list[0] = '爆炒鳝鱼'
# print('将第一道菜改为爆炒鳝鱼后，菜单如下')
# for food in food_list:
#    print(food)

# 替换愿菜单中前两个菜品，分别是 虾仁炒蛋 和 卤牛肉
food_list = ('虾仁炒蛋','卤牛肉','海带排骨汤','油焖大虾','剁椒鱼头')
print('最新的菜单如下:')
for food in food_list:
    print(food)