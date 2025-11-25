favorite_city = {
    '张三':['北京','大连','哈尔滨'],
    '李四':['西安','青海','兰州'],
    '王五':['杭州','苏州','无锡']
}

for user,city in favorite_city.items():
    print(f'{user}喜欢的城市有{city}')