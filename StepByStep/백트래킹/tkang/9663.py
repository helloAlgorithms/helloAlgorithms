import sys
input = sys.stdin.readline

n = int(input())

map_lst = [[0] * (n) for _ in range(n)]
col, up_right, down_left = set(), set(), set()
ans = 0

def dfs(iter):
	global ans
	if iter == n:
		ans += 1
		return

	for i in range(n):
		if i in col or (iter + i) in up_right or (iter - i) in down_left:
			continue

		col.add(i)
		up_right.add(iter + i)
		down_left.add(iter - i)
		map_lst[iter][i] = 1

		dfs(iter + 1)

		col.remove(i)
		up_right.remove(iter + i)
		down_left.remove(iter - i)
		map_lst[iter][i] = 0

dfs(0)

print(ans)