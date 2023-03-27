N = int(input())
trees = [input().split(' ') for _ in range(N)]

def findidx(tree, c):
    for i in range(len(tree)):
        if tree[i][0] == c:
            return i
    return -1

def preorder(node):
    if not node:
        return ;
    print(node[0], end='')
    left = findidx(trees, node[1])
    if left  == -1:
        leftnode = 0
    else:
        leftnode = trees[left]
    right = findidx(trees, node[2])
    if right == -1:
        rightnode = 0
    else:
        rightnode = trees[right]

    preorder(leftnode)
    preorder(rightnode)

def inorder(node):
    if not node:
        return ;
    left = findidx(trees, node[1])
    if left  == -1:
        leftnode = 0
    else:
        leftnode = trees[left]
    right = findidx(trees, node[2])
    if right == -1:
        rightnode = 0
    else:
        rightnode = trees[right]

    inorder(leftnode)
    print(node[0], end='')
    inorder(rightnode)

def postorder(node):
    if not node:
        return ;
    left = findidx(trees, node[1])
    if left  == -1:
        leftnode = 0
    else:
        leftnode = trees[left]
    right = findidx(trees, node[2])
    if right == -1:
        rightnode = 0
    else:
        rightnode = trees[right]

    postorder(leftnode)
    postorder(rightnode)
    print(node[0], end='')

preorder(trees[0])
print("")
inorder(trees[0])
print("")
postorder(trees[0])
