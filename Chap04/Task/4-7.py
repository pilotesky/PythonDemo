# 输出3到30能被3整除的数字
a_list = range(3,31)
for num in a_list:
    if num % 3 == 0:
        print(num)