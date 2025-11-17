# 在字典中存储字典
company_list = {

    'GE':{
        'Location':'America',
        'cn_name':'通用电气'
    },

    'Audi':{
        'Location':'Germany',
        'cn_name':'奥迪'
    },

    'Toyota':{
        'Location':'Japan',
        'cn_name':'丰田'
    }
}

for company_name,company_info in company_list.items():
    print(f'公司名称是{company_name}')
    for address,chinese_name in company_info.items():
        print(address,chinese_name)