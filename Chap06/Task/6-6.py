wait_list = ['Jason','Ray','Clay']
checked_list = ['Stella','Jason','Ray']

for user in wait_list:
    if user in checked_list:
        print(f'{user} 已经注册')
    else:
        print(f'{user} 还没注册')