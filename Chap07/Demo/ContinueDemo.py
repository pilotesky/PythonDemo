# 使用continue 跳出当前循环
# 输出1到10的奇数
currnet_number = 0
while currnet_number < 10:
    currnet_number += 1
    if currnet_number % 2 == 0:
        continue

    print(currnet_number)