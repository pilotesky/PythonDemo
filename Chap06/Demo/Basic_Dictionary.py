computer_info = {
    'motherloand':'华硕',
}
print(f'这款电脑用的主板是{computer_info['motherloand']}')
# 添加一个键值对
computer_info['memory'] = '海力士'
print(f'新添加一项内存的品牌是{computer_info["memory"]}')

# 暂时总结一下
for key,value in computer_info.items():
    print(key,value)

# 创建一个空字典，再向字典添加信息
university_info = {}
university_info['名称'] = '浙江大学'
university_info['城市'] = '杭州'
print(f'这所大学名为{university_info['名称']},所在地是{university_info['城市']}')
# 修改字典中的值
university_info['名称'] = '浙江工业大学'
print(f'这所大学名为{university_info['名称']},所在地是{university_info['城市']}')

# 还有一个键值对没有删除
print(f'所在地是{[university_info['城市']]}')
# 删除键值对
# del university_info['名称']
# print(f'这所大学名为{university_info['名称']}')
