def get_user_info(first_name,last_name,**other_info):
    # 建一个空字典来存储要写入的信息
    user_info = {}
    user_info['姓'] = first_name
    user_info['名'] = last_name
    for key,value in other_info.items():
        user_info[key] = value
    return user_info

my_info = get_user_info('陈','卓伟',
                        job ='信息专员',
                        age = 27,
                        born_city = '湖北汉川')
print(my_info)