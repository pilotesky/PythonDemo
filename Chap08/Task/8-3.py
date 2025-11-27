def make_shirt(size,logo):
    print(f'这件衣服的尺码是{size},衣服上有印刷{logo}的图案')
# 调用
make_shirt('3XL','MLB') # 使用位置实参
make_shirt('2XL',logo='FILA') # 使用关键字实参