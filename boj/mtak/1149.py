n = int(input())
price = []
for _ in range(n):
	r, g, b = map(int, input().split())
	price.append([r, g, b])
minP = float("inf")
def dfs(cnt, color, s):
	global minP
	if cnt == n:
		minP = min([s, minP])
		return 
	s += price[cnt][color]
	for c in range(3):
		if c != color:
			dfs(cnt + 1, c, s)
for i in range(3):
	dfs(0, i, 0)
print(minP)
	
