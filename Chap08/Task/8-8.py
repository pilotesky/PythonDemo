def make_album(artist_name,album_title):
    full_album_info = {'歌手名称':artist_name,'专辑名称':album_title}
    return full_album_info

# 创建一个列表用来存放用户输入的歌手及专辑的字典信息
album_collection = []

# 开始while循环输入
while True:

    # 首先是检查输入的歌手名称
    name = input('请输入歌手名称,如果输入quit则立即退出程序:\n')
    # 如果输入 quit 则立即退出程序
    if name == 'quit':
        print('退出程序')
        break
    # 如果输入非字符内容,则提示用户重新输入
    if name.isdigit():
        print('您的输入有误,请重新输入:\n')
        continue

    # 其次是输入专辑信息
    title = input('请输入专辑名称,如果输入quit则立即退出程序:\n')
    # 如果输入 quit 则立即退出程序
    if title == 'quit':
        print('退出程序')
        break
    # 如果输入非字符内容,则提示用户重新输入
    if title.isdigit():
        print('您的输入有误,请重新输入:\n')
        continue

    new_album = make_album(name,title)
    album_collection.append(new_album)

    # 立即输出刚刚添加的专辑信息
    print(f'最新添加的专辑信息: {new_album}')

print('--------所有的专辑信息如下--------')
for album in album_collection:
    print(album)