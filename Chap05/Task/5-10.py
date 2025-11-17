current_users = ['pilote', 'sonny', 'clay']
new_users = ['Pilote', 'SONNY', 'stealla', 'jason']

# 预处理：创建小写列表
current_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_lower:  # 检查 'pilote' 是否在列表中
        print(f'{user}已经是VIP用户')
    else:
        print(f'{user}还没有注册')