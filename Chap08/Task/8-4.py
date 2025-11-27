def make_shirt(size,logo='我喜欢奥迪'):
    print(f'这件衣服的尺码是{size},默认的印刷了{logo}的图案')
# 默认字样大号
make_shirt('大号')
# 默认字样中号
make_shirt('中号')
# 第三件,不限制尺码和logo
make_shirt('中号','Airbus')