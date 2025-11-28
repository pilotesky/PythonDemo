# 函数直接修改原列表（默认行为）
def travel_plan(city_list):
    while city_list:
        city = city_list.pop()
        print(f'计划去旅游的城市{city}')
    
# 原本计划的城市
my_list = ['北京','上海','广州']
# 开始行动
travel_plan(my_list)
# 旅行完成之后
print(my_list)

# 传入副本，保护原列表
def travel_plan(place_list):
    while place_list:
        place = place_list.pop()
        print(f'计划去旅游的城市{place}')
    
# 原本计划的城市
my_list = ['北京','上海','广州']
# 开始行动
travel_plan(my_list[:])
# 旅行完成之后
print(my_list)