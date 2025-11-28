def make_album(artist,album_name,song_nums=''):
    # 先把已有的录入进来
    album_info = {'歌手名称':artist,'专辑名称':album_name}
    # 如果有歌曲数量的信息就一起添加进来
    if song_nums:
        album_info['歌曲数量'] = song_nums
    # 返回结果
    return album_info

gem = make_album('邓紫棋','泡沫',1)
jason = make_album('蔡依林','第三人称',2)
she = make_album('SHE','你曾是少年')

artist_list = [gem,jason,she]

for target_artist in artist_list:
    print(target_artist)