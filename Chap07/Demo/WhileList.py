# 在列表之间移动元素

# 等待出结果的科目列表
wait_publish_subjects = ['Chinese','Math','English']
# 已经出结果的科目列表
published_subjects = []

# 开始循环
while wait_publish_subjects:
    # 当前科目列表来自等待出结果的科目里面弹出来
    current_subject = wait_publish_subjects.pop()

    # 输出正在处理的科目
    # 不需要对 current_subjects 再做 for 循环，因为它本身就是一个科目名称（字符串），直接打印即可：
    print(f'正在处理的科目有{current_subject}')

    # 向已经出结果的列表追加科目
    published_subjects.append(current_subject)

# 使用for循环来输出已经发布的科目列表
print('已经发布成绩的科目如下:')
for published_subject in published_subjects:
    print(published_subject)