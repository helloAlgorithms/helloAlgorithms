import sys
import string

input = sys.stdin.readline
n = int(input())
tree = {string.ascii_uppercase[i]:[0, 0]for i in range(n)}
for _ in range(n):
	p, l, r = input().strip().split()
	tree[p][0] = l
	tree[p][1] = r
def preorder(node):
	if node != ".":
		preorder.order += node
		preorder(tree[node][0])
		preorder(tree[node][1])
def inorder(node):
	if node != ".":
		inorder(tree[node][0])
		inorder.order += node
		inorder(tree[node][1])
def postorder(node):
	if node != ".":
		postorder(tree[node][0])
		postorder(tree[node][1])
		postorder.order += node
preorder.order = ""
inorder.order = ""
postorder.order = ""
preorder("A")
inorder("A")
postorder("A")
print(preorder.order, inorder.order, postorder.order, sep="\n")