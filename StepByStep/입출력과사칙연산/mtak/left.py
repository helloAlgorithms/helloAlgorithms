input = input()
input_arr_str = input.split()
input_arr_num = []
for i in input_arr_str:
    input_arr_num.append(int(i))
print((input_arr_num[0] + input_arr_num[1]) % input_arr_num[2])
print(((input_arr_num[0] % input_arr_num[2]) + (input_arr_num[1] % input_arr_num[2])) % input_arr_num[2])
print((input_arr_num[0] * input_arr_num[1]) % input_arr_num[2])
print(((input_arr_num[0] % input_arr_num[2]) * (input_arr_num[1] % input_arr_num[2])) % input_arr_num[2])