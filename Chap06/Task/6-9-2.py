# 先建立一个最喜欢的城市对应的空字典
favorite_places = {}

while True:
    
    # 提示用户输入姓名
    name = input('请输入您的姓名:\n')
    if name == 'quit':
        exit()
    
    # 对于用户喜欢的地方先建一个空列表
    place_list = []
    # 提示用户输入地方，限3个
    for time in range(3):
        # 开始输入并开始计数
        place = input(f'{name},请输入你第{time+1}喜欢去的地方是:\n')
        # 对输入进行判断
        if place == 'quit':
            exit()
        # 将客户输入的地方添加到地方列表中
        place_list.append(place)
    # 将客户输入的姓名和其输入的地方进行绑定
    favorite_places[name] = place_list

    # 使用for循环将用户的姓名及其喜欢的地方输出出来
    for username,city in favorite_places.items():
        print(f'{username}最喜欢的城市如下:\n{city}')