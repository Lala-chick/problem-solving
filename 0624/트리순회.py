from collections import defaultdict

def preorder(tree, node):
    if node == '.':
        return
    print(node, end="")
    preorder(tree, tree[node][0])
    preorder(tree, tree[node][1])

def inorder(tree, node):
    if node == '.':
        return
    inorder(tree, tree[node][0])
    print(node, end="")
    inorder(tree, tree[node][1])

def postorder (tree, node):
    if node == '.':
        return
    postorder(tree, tree[node][0])
    postorder(tree, tree[node][1])
    print(node, end="")

N = int(input())
tree = defaultdict()
for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)

preorder(tree, "A")
print()
inorder(tree, "A")
print()
postorder(tree, "A")