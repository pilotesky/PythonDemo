def make_album(artist,album_name):
    album_info = {'歌手名称':artist , '专辑名称':album_name}
    return album_info

gem = make_album('邓紫棋','泡沫')
jason = make_album('蔡依林','第三人称')
she = make_album('SHE','你曾是少年')

artist_list = [gem,jason,she]

for target_artist in artist_list:
    print(target_artist)