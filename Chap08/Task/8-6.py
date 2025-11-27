def city_country(city_name,country_name):
    relation_mapping = f'{city_name},{country_name}'
    return relation_mapping
Hangzhou = city_country('杭州','中国')
Tokyo = city_country('东京','日本')
London = city_country('伦敦','英国')

city_list = [Hangzhou,Tokyo,London]
for city in city_list:
    print(city)