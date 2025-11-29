def build_computer(*parts):
    print('组装一台电脑需要以下零件:')
    for part in parts:
        print(part)
build_computer('CPU')
build_computer('主板','内存','硬盘')
build_computer('电源','散热器','机箱','硬盘')
