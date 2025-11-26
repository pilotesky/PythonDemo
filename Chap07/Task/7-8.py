# 给客户用展示菜单
food_menu = ['东坡肉','锅包肉','土豆炖牛腩']
# 已经出餐的菜品
finished_food_menu = []

while food_menu:
    
    # 正在制作的菜品来自展示菜单
    # 如果需按菜单顺序 可用 pop(0)
    cooking_food = food_menu.pop()
    print(f'正在制作的菜品有:{cooking_food}')

    finished_food_menu.append(cooking_food)

print('已经出餐的菜品有:')
for food in finished_food_menu:
    print(food)