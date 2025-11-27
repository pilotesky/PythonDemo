# 定义一个解释用的函数 带有city 城市名称 country 国家名称(默认值) 总计两个形参
def describe_city(city,country='中国'):
    # 函数的用处是输出结果,解释城市所在国家(默认值) 到这里 两个参数都还是形参
    print(f'{city}这座城市是在{country}这个国家')
# 开始传参 这里是实参 并且直接输出结果
describe_city('杭州','中国')
# 传参并且修改默认值
describe_city('伦敦','英国')
describe_city('洛杉矶','美国')