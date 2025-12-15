# 组合
class Ranking():
    def __init__(self,world_rank=0,national_rank=0):
        self.world_rank = world_rank
        self.national_rank = national_rank

    def show_ranking(self):
        print(f'这所学校在国际上排名{self.world_rank}名,在国内排名{self.national_rank}')

# 父类
class University():

    # 初始化属性
    def __init__(self,title,location,world_rank=0,national_rank=0):
        self.title = title
        self.location = location
        self.ranking = Ranking(world_rank,national_rank)
    
    # 介绍
    def describe_university(self):
        print(f'这所学校的名称是{self.title},是在{self.location},这所学校在国际上排名是{self.ranking.world_rank},在国内的排名是{self.ranking.national_rank}')


# 子类 私立大学
class Private_University(University):

    # 继承父类初始化
    def __init__(self, title, location,world_rank=0,national_rank=0):
        super().__init__(title,location,world_rank,national_rank)

    # 自己的方法来介绍
    def describe_private_univeristy(self):
        print(f'这是一所私立大学,学校名称是{self.title},是在{self.location},这所学校在国际上排名是{self.ranking.world_rank},在国内的排名是{self.ranking.national_rank}')
    # 重写父类的方法
    def describe_university(self):
        print(f'{self.title}是一所顶级学校')

# 子类 公立大学
class Public_University(University):

    # 继承父类初始化
    def __init__(self,title,location,world_rank=0,national_rank=0):
        super().__init__(title,location,world_rank,national_rank)

    # 自己的方法来介绍
    def describe_public_university(self):
        print(f'这是一所公立大学,学校名称是{self.title},是在{self.location},这所学校在国际上排名是{self.ranking.world_rank},在国内的排名是{self.ranking.national_rank}')
    # 重写父类的方法
    def describe_university(self):
        print(f'{self.title}是一所顶级学校')

Caltech = Private_University('加州理工学院','美国',2,3)
Caltech.describe_private_univeristy()
# 重写父类的方法
Caltech.describe_university()

UCL = Public_University('伦敦大学国王学院','英国',5,2)
UCL.describe_public_university()
# 重写父类的方法
UCL.describe_university()