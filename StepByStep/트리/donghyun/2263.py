import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
inorder = {j: i for i, j in enumerate(map(int, input().split()))}
postorder = list(map(int, input().split()))
def preorder(s_in, e_in, s_post, e_post):
	if e_in >= s_in and e_post >= s_post:
		parent = postorder[e_post]
		preorder.print.append(parent)
		i = inorder[parent]
		preorder(s_in, i - 1, s_post, s_post + (i - 1 - s_in))
		preorder(i + 1, e_in, s_post + (i - s_in), e_post - 1)
preorder.print = []
preorder(0, n - 1, 0, n - 1)
print(*preorder.print)