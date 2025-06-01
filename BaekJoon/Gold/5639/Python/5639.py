# no. 5639: 이진 검색 트리 (Gold IV)
# 이진 검색 트리를 전위 순회한 결과가 주어졌을때 -> 후위 순회한 결과를 구해라
# 트리의 삽입까지만 구현, 후위 순회하면됨

from sys import stdin
from sys import setrecursionlimit
input = stdin.readline
setrecursionlimit(10**5)

tree = {}
root = None
def insert(val, node=None):
    if node == None:
        global root
        root = val
        tree[root] = []
        return
    if val > node:
        if not tree[node]:
            tree[node] = [None, val]
            tree[val] = []
        elif tree[node][1] == None:
            tree[node][1] = val
            tree[val] = []
        else:
            insert(val, tree[node][1])
    else:
        if not tree[node]:
            tree[node] = [val, None]
            tree[val] = []
        elif tree[node][0] == None:
            tree[node][0] = val
            tree[val] = []
        else:
            insert(val, tree[node][0])

def traverse(node):
    if tree[node] and tree[node][0] != None:
        traverse(tree[node][0])
    if tree[node] and tree[node][1] != None:
        traverse(tree[node][1])
    print(node)
    
num = input().rstrip()
while num:
    insert(int(num), root)
    num = input().rstrip()

traverse(root)