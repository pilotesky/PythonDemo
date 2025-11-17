my_food = ['锅包肉','黄鱼烧年糕','干锅花菜']
friend_food = my_food[:]
my_food.append('红烧狮子头')
friend_food.append('麻婆豆腐')
print(f'我下单的菜品包括{my_food}')
print(f'朋友下单的菜品如下:')
for food in friend_food:
    print(food)

