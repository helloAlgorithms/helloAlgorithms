a, b, c = map(int, input().split())
def dq(a, b, c):
	if b == 1:
		return a % c
	if b == 2:
		return a * a % c
	return dq(a, b//2, c)**2 * a**(b%2) % c
print(dq(a, b, c))