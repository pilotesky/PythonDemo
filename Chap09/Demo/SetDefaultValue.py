class Employee:
    
    # 初始化属性
    def __init__(self,name,age,grade_university='Caltech'):
        self.name = name
        self.age = age
        self.grade_university = grade_university

    # 显示员工信息
    def display_info(self):
        print(f'姓名: {self.name}, 年龄: {self.age}, 毕业院校: {self.grade_university}')

    # 通过方法修改属性值
    def update_grade_university(self, new_university):
        self.grade_university = new_university

    # 通过方法让属性的值增加
    def celebrate_birthday(self):
        self.age += 1
        print(f'祝{self.name}生日快乐！年龄增加到{self.age}岁。')

# 创建Employee对象，未指定grade_university，使用默认值
xiaomi = Employee('小米',25)
xiaomi.display_info()

# 直接修改属性值
xiaomi.grade_university = 'IC'
xiaomi.display_info()

# 使用方法修改属性值
xiaomi.update_grade_university('MIT')
xiaomi.display_info()

# 使用方法增加年龄
xiaomi.celebrate_birthday()