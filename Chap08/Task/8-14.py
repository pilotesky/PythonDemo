def get_car_info(brand,model,**other_info):
    car_info = {}
    car_info['car_brand'] = brand
    car_info['car_model'] = model
    for key,value in other_info.items():
        car_info[key] = value
    return car_info

audi = get_car_info('Audi','A8',
                    color = 'black',
                    power = 'electric',
                    year = 2025)
print(audi)