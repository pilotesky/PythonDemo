# 设置默认值属性
class Airport():

    def __init__(self,cn_name,code):
        self.cn_name = cn_name
        self.code = code
        # 设置默认值
        self.location = '杭州'
    
    def describe_airport(self):
        print(f'这座机场的中文名称是{self.cn_name} 它的通用代码是{self.code} 其位于{self.location}')

xiaoshan = Airport('杭州萧山国际机场','HGH')
xiaoshan.describe_airport()