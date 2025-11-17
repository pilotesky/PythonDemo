river_info = {
    '长江':'中国',
    '贝加尔湖':'俄罗斯',
    '湄公河':'泰国',
    '泰晤士河':'英国',
    '亚马逊河':'巴西',
    '莱茵河':'德国'
}
# 先万兆的输出一遍
for river_name,country in river_info.items():
    print(f'{river_name}流经{country}')

print('------------------')

# 输出所有河流名称
print('涉及的河流如下:')
for river_name in river_info.keys():
    print(river_name)

print('------------------')
print('涉及的国家如下:')
for country in river_info.values():
    print(country)