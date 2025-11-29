def make_album(artist,album_name,songs=None):
    album_info = {
        '歌手名称':artist,
        '专辑名称':album_name,
    }
    if songs is not None:
        album_info['歌曲数量'] = songs
    return album_info

gem = make_album('邓紫棋','泡沫',1)
print(gem)
eson = make_album('陈奕迅','孤独患者')
print(eson)