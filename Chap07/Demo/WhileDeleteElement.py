# 使用while函数删除指定元素
airport_list = ['HGH','SHA','PVG','HKG','PEK']
while 'PEK' in airport_list:
    airport_list.remove('PEK')
print(airport_list)