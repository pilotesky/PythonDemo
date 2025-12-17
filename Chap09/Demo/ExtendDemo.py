# 组合
class Ranking:

    def __init__(self,world_rank,national_rank):
        self.world_rank = world_rank
        self.national_rank = national_rank

    def describe_rank(self):
        print(f'这所学校在全球的排名是第{self.world_rank},在国内的全球排名是{self.national_rank}')

# 父类
class University:

    def __init__(self,title,location,ranking):
        self.title = title
        self.location = location
        self.ranking = ranking
    
    def describe_university(self):
        print(f'这所学校的全称是{self.title},位于{self.location},其全球排名是第{self.ranking.world_rank}名,其国内排名是第{self.ranking.national_rank}名')

# 子类
class Public_University(University):

    def __init__(self, title, location,ranking):
        super().__init__(title, location,ranking)

    def describe_public_university(self):
        print(f'这所公立大学名称是:{self.title},位于{self.location},其全球排名是第{self.ranking.world_rank}名,其国内排名是第{self.ranking.national_rank}名')
    # 重写父类方法
    def describe_university(self):
        print('这是一所顶级公立大学')

class Private_University(University):

    def __init__(self, title, location,ranking):
        super().__init__(title, location,ranking)

    def describe_private_university(self):
        print(f'这所私立大学名称是:{self.title},位于{self.location},其全球排名是第{self.ranking.world_rank}名,其国内排名是第{self.ranking.national_rank}名')

    # 重写父类方法
    def describe_university(self):
        print('这是一所顶级私立大学')

# 调用父类
fudan_ranking = Ranking(43,3)
FDU = University('复旦大学','中国上海',fudan_ranking)
FDU.describe_university()

# 调用子类 公立大学
ucla_ranking = Ranking(27,7)
UCLA = Public_University('加州大学洛杉矶分校','美国加州',ucla_ranking)
UCLA.describe_public_university()
# 重写父类方法
UCLA.describe_university()

# 调用子类 私立大学
caltech_ranking = Ranking(6,6)
Caltech = Private_University('加州理工学院','美国加州',caltech_ranking)
Caltech.describe_private_university()
# 重写父类方法
Caltech.describe_university()