# 切片
car_list = ['bmw','audi','byd']

print(f'第一个品牌是{car_list[0]}')
print(f'最后一个品牌是{car_list[-1]}')

print(f'最前面的两个品牌是{car_list[:2]}')  # 修正为更清晰的写法
print(f'最后面的两个品牌是{car_list[1:]}')

print('---------------------')

# 遍历切片
college_list = ['Soft College','Building Design College','Medical College','Math College']
# 先把所有的学院名称打出来
print('学院信息如下:')
for college in college_list:
    print(f'{college}')
# 截取最前面的两个
print('排在前二的学院如下:')
for college in college_list[:2]:
    print(college)

print('---------------------')

# 复制切片
my_food = ['pizza','dumpling','hot dog']
print(f'我已经下单的是:\n{my_food}')
fried_food = my_food[:]
print('朋友下单的是:')
for food in fried_food:
    print(f'{food}')

