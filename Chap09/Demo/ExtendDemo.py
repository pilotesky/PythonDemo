class School():

    def __init__(self,title,location):
        self.title = title
        self.location = location
    
    def descirbe_school(self):
        print(f'学校名称是{self.title},学校位于{self.location.get_address()}')

# 直接调用父类
target_school = School('清华大学','北京')
target_school.descirbe_school()

# 子类继承父类
class College(School):

    def __init__(self,title,location,top_college):
        super().__init__(title,location)  # 调用父类的初始化方法
        self.top_college = top_college  # 子类新增属性，说明强势学院

    def describe_college(self):
        print(f'学院名称是{self.title},学院位于{self.location},强势学院有{self.top_college}')

class University(School):
    
    def __init__(self,title,location,master_major):
        super().__init__(title,location)  # 调用父类的初始化方法
        self.master_major = master_major  # 子类新增属性，说明硕士专业

    def describe_university(self):
        print(f'大学名称是{self.title},大学位于{self.location},硕士专业有{self.master_major}个')

    def descirbe_school(self):  # 重写父类方法
        print(f'这是一个著名的大学，名称是{self.title},位于{self.location},硕士专业有{self.master_major}个')

# 创建子类实例
IC = College('帝国理工','英国','EE&CS')
IC.describe_college()
PKU = University('北京大学','北京',100)
PKU.describe_university()
UCLA = University('加州大学洛杉矶分校','美国',200)
UCLA.descirbe_school()  # 调用重写的方法