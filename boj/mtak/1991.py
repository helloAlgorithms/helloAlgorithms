import sys
input = sys.stdin.readline
cnt = int(input())
get = []
for _ in range(cnt):
    get.append(input().split())
class Node():
    def __init__(self, item, l, r):
        self.item = item
        self.l = l
        self.r = r
def preorder(node):
    print(node.item, end="")
    if node.l != ".":
        preorder(tree[node.l])
    if node.r != ".":
        preorder(tree[node.r])
def inorder(node):
    if node.l != ".":
        inorder(tree[node.l])
    print(node.item, end="")
    if node.r != ".":
        inorder(tree[node.r])
def postorder(node):
    if node.l != ".":
        postorder(tree[node.l])
    if node.r != ".":
        postorder(tree[node.r])
    print(node.item, end="")
tree = {}
for item, left, right in get:
    tree[item] = Node(item, left, right)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

