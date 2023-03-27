N = int(input())
M = int(input())
min_count = 0x3f3f3f3f
buttons = {i for i in range(10)}

if M:
    buttons -= set(map(int, input().split(' ')))    

min_count = min(min_count, abs(100 - N))

def check(channel_num):
    global min_count
    for button in buttons:
        tmp_num = channel_num + str(button)
        min_count = min(min_count, abs(N - int(tmp_num)) + len(tmp_num))

        if len(tmp_num) < 6:
            check(tmp_num)

check('') if M < 10 else ''
print(min_count)