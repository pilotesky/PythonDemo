# 计算1到10的平方书

# 第一种办法
squares = [] # 先定义一个空列表
# for 循环遍历1到10的数据
for value in range(1,11):
    # 构成列表的元素等于value的平方
    square = value ** 2
    # 将元素添加到空列表中
    squares.append(square)
# 输出列表
print(squares)

# 第二种办法 使用列表解析
# value是依次取值 range(1,11) 中的每个元素,squares是由value为基础的求平方获得
squares = [value ** 2 for value in range(1,11)]
print(squares)