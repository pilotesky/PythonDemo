prompt = '请告诉我内容，我将复述一遍给你\n'

# 设置一个flag
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)