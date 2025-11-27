# 默认值 这里 college 是默认值
def get_student_info(name,level,college='Computer Science And Technolog'):
    # 输出相关信息
    print(f'{name}这位学生目前攻读{level}课程,是{college}这个学院的')
get_student_info('张三','Master')