import sys
input = sys.stdin.readline

n = int(input())
nodes = {}
for _ in range(n):
    root, left, right = input().split()
    nodes[root] = (left, right)

def preorder_traverse(root):
    if root == '.':
        return
    print(root, sep='', end='')
    preorder_traverse(nodes[root][0])
    preorder_traverse(nodes[root][1])

def inorder_traverse(root):
    if root == '.':
        return
    inorder_traverse(nodes[root][0])
    print(root, sep='', end='')
    inorder_traverse(nodes[root][1])

def postorder_traverse(root):
    if root == '.':
        return
    postorder_traverse(nodes[root][0])
    postorder_traverse(nodes[root][1])
    print(root, sep='', end='')

preorder_traverse('A')
print()
inorder_traverse('A')
print()
postorder_traverse('A')
print()
