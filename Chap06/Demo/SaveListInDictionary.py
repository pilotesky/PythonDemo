# 在字典中存储列表
college_info = {
    'title':'Calth',
    'top_subject':['math','physics','computer science']
}

print(f'这所学院的名称是{college_info['title']}')
print(f'{college_info["title"]}的强势学科如下:')
for subject in college_info['top_subject']:
    print(subject)