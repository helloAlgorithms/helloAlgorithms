n = int(input())
cases = [0] * 1001
cases[1] = 1
cases[2] = 2 
for i in range(3, n + 1):
	cases[i] = (cases[i - 1] + cases[i - 2]) % 10007
print(cases[n])

