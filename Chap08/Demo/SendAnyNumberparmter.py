# 传递任意数量的实参
def build_computer(*parts):
    # 输出所有零件
    print(f'组装电脑需要如下零件:')
    for part in parts:
        print(f'- {part}')

build_computer('CPU')
build_computer('Memory','Disk')

# 结合使用位置实参和任意数量实参
def make_cake(size,*fruit_list):
    print(f'制作一个{size}寸大小的蛋糕需要如下材料')
    print('此蛋糕包含以下水果:')
    for fruit in fruit_list:
        print(fruit)
make_cake(12,'草莓','芒果')

# 使用任意数量的关键字实参
def get_brand_info(name,model,**other_info):
    brand_info = {}
    brand_info['品牌名称'] = name
    brand_info['代表型号'] = model
    for key,value in other_info.items():
        brand_info[key] = value
    return brand_info

tesla = get_brand_info('特斯拉','Model S',
                       location = 'California US')
print(tesla)

# * 用于传递任意数量的“值”（位置实参），
# ** 用于传递任意数量的“键值对”（关键字实参）。