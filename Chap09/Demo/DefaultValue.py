# 给属性设置默认值
class User():
    
    # 初始化属性
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
        self.university = '清华大学'  # 设置默认值
    
    # 描述用户信息
    def describe_user(self):
        print(f'用户的姓名是{self.name},年龄是{self.age},所在地是{self.location}')

    # 说明毕业院校
    def grade_university(self):
        print(f'{self.name}毕业于{self.university}')

    # 通过方法修改属性
    def update_grade_university(self,new_university):
        self.university = new_university
        print(f'{self.name}的毕业院校已更新为{self.university}')

    # 通过方法让属性的值递增
    def increment_age(self,years):
        self.age += years
        print(f'{self.name}的年龄已增加到{self.age}岁')


friend = User('小明',21,'北京')
friend.describe_user()
friend.grade_university()

# 修改属性值 以修改默认值为例
friend.university = '北京大学'
friend.grade_university()

# 通过方法修改属性值
friend.update_grade_university('复旦大学')
friend.grade_university()

friend = User('小红',19,'上海')
friend.increment_age(2)
friend.describe_user()