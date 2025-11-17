# 创建1到10的立方列表
target_list = []
for value in range(1,11):
    element = value ** 3
    target_list.append(element)
for num in target_list:
    print(num)

# 使用列表解析
target_list = [element **3 for element in range(1,11)]
print(target_list)