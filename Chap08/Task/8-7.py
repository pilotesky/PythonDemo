def make_album(artist_name,album_name):
    album_info = {'歌手名称':artist_name,'专辑名称':album_name}
    return album_info
    # 等价写法
    # return {'歌手名称':artist_name,'专辑名称':album_name}

gem = make_album('邓紫棋','泡沫')
eson = make_album('陈奕迅','孤独患者')
Jay = make_album('周杰伦','七里香')

artist_list = [gem,eson,Jay]
for artist in artist_list:
    print(artist)