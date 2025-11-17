# 检查待办事项列表
wait_list = []

if wait_list:
    print("今天要做的事情：")
    for task in wait_list:
        print(f"- {task}")
else:
    print("太棒了！今天没有待办事项，可以休息啦！")