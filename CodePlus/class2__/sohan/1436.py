N = int(input())

six = "666"
shom_index = 1
index = 0

if N == 1:
    print(six)
    exit(0)

while True:
    num_front = ""
    num_back = ""
    power = 0
    number = str(index)
    if number[-1] == '6':
        for _ in reversed(number):
            if _ != '6':
                break
            power = power + 1
        number_index = len(number) - power - 1
        if number_index >= 0:
            num_front =''.join(map(str, number[:number_index + 1]))
        for _ in range(10 ** power):
            if shom_index == N:
                num_back = '{:0>{length}}'.format(str(_), length = power)
                print(num_front + six + num_back)
                exit(0)
            shom_index = shom_index + 1
        index = index + 1
    if shom_index == N:
        num_front = str(index)
        print(num_front + six + num_back)
        exit(0)
    shom_index = shom_index + 1
    index = index + 1
