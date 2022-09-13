import sys

sys.setrecursionlimit(10**6)
preorder = list(map(int, open(0).read().split()))
def postorder(start, end):
	if start <= end:
		parent = preorder[start]
		mid = start + 1
		while mid <= end and parent > preorder[mid]:
			mid += 1
		postorder(start + 1, mid - 1)
		postorder(mid, end)
		print(parent)
postorder(0, len(preorder) - 1)