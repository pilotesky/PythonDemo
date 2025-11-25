prompt = '请告诉我内容，我将重复一遍告诉你\n如果输入quit则会立即退出程序：'
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':  # 只有在不是退出指令时才打印
        print(message)