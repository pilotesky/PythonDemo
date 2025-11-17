xiaomi = {
    'pet_type':'dog',
    'pet_owner':'老王'
}

sunny = {
    'pet_type':'cat',
    'pet_owner':'张三'
}

dragon = {
    'pet_type':'snake',
    'pet_owner':'李四'
}

pet_list = [xiaomi, sunny, dragon]

for pet in pet_list:
    pet_type = pet['pet_type']
    pet_owner = pet['pet_owner']
    print(f'这个宠物的类型是{pet_type},宠物的主人是{pet_owner}')