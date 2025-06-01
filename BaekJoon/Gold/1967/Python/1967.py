# no. 1967: 트리의 지름 (Gold IV)

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())

tree = {i: {} for i in range(1, n+1)}
for _ in range(n-1):
    root, child, weight = map(int, input().split())
    tree[root][child] = weight
    tree[child][root] = weight

def dfs(root, dist=None):
    if dist == None:
        dist = {root: 0}
    for child, weight in tree[root].items():
        if child in dist:
            continue
        dist[child] = dist[root] + weight
        dfs(child, dist)
    return max(dist.items(), key=lambda x: x[1])

a = dfs(1)[0]
dist = dfs(a)[1]
print(dist)