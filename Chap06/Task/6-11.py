cities = {
    'Hangzhou':{
        'country':'China',
        'population':'千万级',
        'fact':'历史名城'
    },
    'Los Angel':{
        'country':'America',
        'population':'千万级',
        'fact':'好莱坞所在地'
    },
    'London':{
        'country':'United Kingdom',
        'population':'千万级',
        'fact':'老牌国家首都'
    }
}

for city_name,description in cities.items():
    # 如果有使用单引号的情况下，建议不要重复使用可以加入双引号
    print(f"{city_name}这座城市相关说明如下:")
    print(f"其归属于{description['country']}")
    print(f"其人口规模是{description['population']}")
    print(f"它是{description['fact']}")