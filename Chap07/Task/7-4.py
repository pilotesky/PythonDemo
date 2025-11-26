message = '请输入您想添加的食材:\n'

active = True
while active:
    food = input(message).strip() # 去除空格
    if food == 'quit':
        active = False
    else:
        print(f'我们将{food}添加到菜品中')