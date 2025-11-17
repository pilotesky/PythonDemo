# 先给出定义
programming_dictionary = {
    'Java':'后端语言',
    'HTML':'文本标记语言',
    'Spring':'后端框架',
    'Python':'脚本语言',
    'VUE':'前端框架'
}

# 输出出来
for language,description in programming_dictionary.items():
    print(f'{language}的中文定义是\n{description}')

print('----------------------------')

# 6-4
print('此字典中涉及的技术如下:')
for language in programming_dictionary.keys():
    print(language)
print('对应的中文解释是:')
for description in programming_dictionary.values():
    print(description)
programming_dictionary['SQL SERVER'] = '微软开发的数据库'
programming_dictionary['Oracle'] = '甲骨文开发的数据库'
programming_dictionary['Panda'] = 'Python用于数据库分析的一个库'
programming_dictionary['Go'] = '谷歌开发的一个编程语言'
programming_dictionary['Ubuntu'] = '最流行的Linux发行版之一'
for title,description in programming_dictionary.items():
    print(f'{title}的中文解释是{description}')