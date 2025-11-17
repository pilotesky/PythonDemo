user_list = ['admin','root','pilote','clay','jason']

if not user_list:
    print('我们需要推广此游戏，需要更多注册用户')
else:
    for user in user_list:
        if user == 'admin':
            print(f'{user} 欢迎管理员登录，是否需要检查系统状态')
        else:
            print(f'{user} 欢迎游戏玩家登录')