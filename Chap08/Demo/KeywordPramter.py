# 关键字实参 demo
# 定义一个获取学生信息的函数 里面带了3个函数，其中一个是关键字实参
def get_student_info(name,college,location):
    # 输出学生信息
    print(f'{name}这位学生就读于{college}学院,老家是{location}')
# 开始带入信息并输出 这里location赋值的杭州就是关键字实参
get_student_info('张三','经管',location='杭州')