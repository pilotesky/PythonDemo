# 返回值
def get_formatted_name(first_name,last_name):
    full_name = first_name + last_name
    return full_name
cyw = get_formatted_name('陈','郁文')
print(cyw)

# 让实参变成可选的
def describe_college(name,location,top_college=''):
    if top_college:
        full_college_info = f'{name}这个学院位于{location},其强势的学院是{top_college}'
    else:
        full_college_info = f'{name}这个学院位于{location}'
    return full_college_info
zju = describe_college('浙江大学','杭州市','计算机学院')
fdu = describe_college('复旦大学','上海')
# 添加到一个列表中
university_list = [zju,fdu]
# for循环输出
for university in university_list:
    print(university)

# 返回字典
def airport_description(cn_name,airport_code):
    full_airport_info = {'中文名称: ':cn_name,'机场代码: ':airport_code}
    return full_airport_info
hk = airport_description('香港国际机场','HKG')
print(hk)

# 结合使用函数和while循环
def get_employee_info(employee_name,age,location):
    full_employee_info = f'{employee_name}这名员工的年龄是{age},其出生地是{location}'
    return full_employee_info
# 开始循环
while True:

    e_name = input('请输入你的姓名:\n')
    # 如果输入 quit 则立即结束程序
    if e_name == 'quit':
        print('您选择退出,程序结束')
        break
    # 如果输入非字符内容则提示重新输入
    if e_name.isdigit():
        print('你的输入有误,请重新输入')
        continue

    e_age = input('请输入你的年龄:\n')
    # 如果输入 quit 则立即结束程序
    if e_age == 'quit':
        print('您选择退出,程序结束')
        break
    # 如果输入非数字内容则提示重新输入
    if not e_age.isdigit():
        print('你的输入有误,请重新输入')
        continue

    e_location = input('请输入你的出生地:\n')
    if e_location == 'quit':
        print('您选择退出,程序结束')
        break
    # 如果输入非字符内容则提示重新输入
    if  e_location.isdigit():
        print('你的输入有误,请重新输入')
        continue
    # 输出收集到的结果  在循环里面 输入完成一次后就立即输出
    result = get_employee_info(e_name, e_age, e_location)
    print(result)