# 显示列表的函数 (保持不变)
def show_actors(actors):
    for actor in actors:
        print(actor)

# 修改后的 make_great() 函数：接收副本，返回修改后的新列表
def make_great(actors_copy):  # 参数名改为 actors_copy 更清晰
    """接收一个列表副本，返回修改后的新列表"""
    # 创建一个新列表来存放修改后的内容
    modified_list = []
    for actor in actors_copy:
        modified_list.append(f'the great {actor}')  # 或者用列表推导式更简洁
    return modified_list  # ← 关键：返回新列表！

# 原始演员列表
original_actors = ['张三','李四','王五']  # ← 建议改名为 original_actors，更清晰

# 在修改前先显示原始列表
print("=== 原始列表 ===")
show_actors(original_actors)

# 调用 make_great()，传入副本，并接收返回值
great_actors = make_great(original_actors[:])  # ← 传入副本！并接收返回值！

# 显示修改后的列表
print("\n=== 添加了 'the great' 的列表 ===")
show_actors(great_actors)

# 再次显示原始列表，确认它没有被修改
print("\n=== 再次确认原始列表未变 ===")
show_actors(original_actors)