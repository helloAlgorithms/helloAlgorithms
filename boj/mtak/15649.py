n, m = map(int, input().split())
arr = [i for i in range(1,n + 1)]
visited = [False] * n
toPrint = list()
cnt = 0

def printToPrint():
	for i in toPrint:
		print(i, end = " ")
	print("")
	return 

def dfs(_cnt):
	if _cnt == m:
		printToPrint()
		return
	for i in range(n):
		if visited[i]:
			continue
		visited[i] = True
		toPrint.append(arr[i])
		dfs(_cnt + 1)
		toPrint.pop()
		visited[i] = False

dfs(0)
