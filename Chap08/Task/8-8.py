def make_album(artist,album_name):
    album_info = {'歌手名称':artist,'专辑名称':album_name}
    return album_info

# 先定义一个集合 用来存储输入的信息
album_collection = {}

while True:

    # 输入歌手信息
    artist_name = input('请输入歌手名称:\n')
    if artist_name == 'quit':
        print('您选择退出,程序退出')
        break
    if artist_name.isdigit():
        print('您的输入有误,请重新输入')
        continue

    # 输入专辑信息
    album_title = input('请输入专辑名称:\n')
    if album_title == 'quit':
        print('您选择退出,程序退出')
        break
    if album_title.isdigit():
        print('您的输入有误,请重新输入')
        continue

    # 完整的专辑信息是来自用的输入 artist_name 歌手名词性 album_title 专辑名称
    full_album_info = make_album(artist_name,album_title)
    # 向空的专辑集合中添加键值对，键是歌手名称 值是[歌手:专辑名称]这个键值对
    # 这里也可以选择等于album_title 只是存储的结构变
    # 按照现有的结构是 邓紫棋 = {'邓紫棋','泡沫'}
    # 如果是等于album_title 存储结构将变为 邓紫棋 = 泡沫
    album_collection[artist_name] = full_album_info
    # 输出完整的专辑信息
    print(full_album_info)