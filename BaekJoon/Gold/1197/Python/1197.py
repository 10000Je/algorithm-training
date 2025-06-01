# no. 1197: 최소 스패닝 트리 (Gold IV)
# 그래프가 주어졌을 때, 최소 스패닝 트리의 가중치의 합을 구하는 문제
# 프림 알고리즘을 풀면 쉽게 풀릴거 같긴한데
# 그래도 union-find 알고리즘에 적응해야 하므로 크루스칼 알고리즘으로 풀어보고자 한다.

# 싸이클 판별법이 조금 어렵다.
# 간선의 양 끝점의 루트노드가 같다면, 싸이클로 판정할 수 있다.
# findroot 알고리즘의 구현을 위해선 mst의 자료구조를 어떻게 작성해야할까
# mst[child] = parent 형식으로 구현하자

from sys import stdin
input = stdin.readline

v, e = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(e)]
edges.sort(key=lambda x:x[2])

parent = [i for i in range(v+1)]
rank = [0 for _ in range(v+1)]

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if rank[a_root] == rank[b_root]:
        parent[b_root] = a_root
        rank[a_root] += 1
    else:
        child = min(a_root, b_root, key=lambda x:rank[x])
        root = max(a_root, b_root, key=lambda x:rank[x])
        parent[child] = root

cost = 0
for edge in edges:
    start, end, weight = edge
    if find(start) == find(end): continue
    union(start, end)
    cost += weight

print(cost)