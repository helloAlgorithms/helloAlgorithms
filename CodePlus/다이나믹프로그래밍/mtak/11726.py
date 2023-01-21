import sys
sys.setrecursionlimit(10000)
n = int(input())
n_cases = 0
def dfs(w, h, cnt):
	global n_cases
	if w == n and h == 2 and cnt == n:
		n_cases += 1
		return 
	if cnt == n :return 
	for i in ['v', 'h']:
		th = h
		tw = w
		if i == 'v':
			if not (th == 0 or th == 2): continue
			th = 2
			tw += 1
		else:
			if th == 2 or tw == 0:
				tw += 2
				th = 1
			else:
				th += 1
		dfs(tw, th ,cnt + 1)
dfs(0, 0, 0)
print(n_cases%1007)
