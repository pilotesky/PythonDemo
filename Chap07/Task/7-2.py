count_customers = input('欢迎光临，请您告诉我本次宴请的总人数是几位?')
if int(count_customers) >= 1 and int(count_customers)<=8:
    print('您好,欢迎光临')
elif int(count_customers) > 8:
    print('抱歉,今天没有位置了')
else:
    print('您告知的信息不对')