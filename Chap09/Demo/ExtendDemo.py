# 组合
class Ranking:
    def __init__(self, world_rank = 0 , national_rank = 0):
        self.world_rank = world_rank
        self.national_rank = national_rank
    
    def describe_rank(self):
        print(f'这所学校的世界排名是第{self.world_rank}名,国内排名是第{self.national_rank}名')

# 父类
class University:
    # 父类 初始化
    def __init__(self,title,location,rank):
        self.title = title
        self.location = location
        self.rank = rank
    # 父类 自己的方法
    def describe_university(self):
        print(f'学校全名是{self.title},位于{self.location}')
        self.rank.describe_rank()

# 子类 私立大学
class Private_University(University):

    # 子类 私立大学初始化
    def __init__(self, title, location, rank):
        super().__init__(title, location, rank)
    # 子类 私立大学自己的方法
    def describe_private_university(self):
        print(f'这所私立学校全名是{self.title},位于{self.location}')
        self.rank.describe_rank()

    def describe_university(self):
        print(f'{self.title}是一所顶级私立大学')
        self.rank.describe_rank()

# 子类 公立大学
class Public_University(University):

    # 子类 公立大学初始化
    def __init__(self, title, location, rank):
        super().__init__(title, location, rank)

    # 子类 公立大学自己的方法
    def describe_public_university(self):
        print(f'这所公立大学的名称是{self.title},位于{self.location}')
        self.rank.describe_rank()

    def describe_university(self):
        print(f'{self.title}是一所顶级公立大学')
        self.rank.describe_rank()

zju_rank = Ranking(world_rank=50,national_rank=5)
caltech_rank = Ranking(world_rank=20,national_rank=10)
ucla_rank = Ranking(world_rank=10,national_rank=5)

ZJU = University('浙江大学','杭州',zju_rank)
ZJU.describe_university()

Caltech = Private_University('加州理工学院','美国加州',caltech_rank)
Caltech.describe_private_university()
Caltech.describe_university()

UCLA = Public_University('加州大学洛杉矶分校','美国加州',ucla_rank)
UCLA.describe_public_university()
UCLA.describe_university()