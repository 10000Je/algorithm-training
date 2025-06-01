# no. 1647: 도시 분할 계획 (Gold IV)
# 최스 스패닝 트리로 접근
# 먼저 주어진 간선들로 최소스패닝트리를 만들면, 한 마을 안에서
# 최소한의 간선들의 가중치의 합으로 연결된 트리가 만들어진다.
# 이때 한 간선을 끊으면, 2개의 마을로 나누어지며, 길의 유지비의 합을 최소로
# 하기 위해선, 가장 가중치가 큰 간선 하나를 끊어야 한다
# 한개 이상 끊게되면 마을이 3개 이상이 되므로 한개만 끊어야 한다

# 후기:
# 체감 난이도: Gold IV
# 분할이라는 단어로 사람을 헷갈리게 하지만, 사실 트리의 모습을 잘 생각해보면
# 쉽게 풀리는 문제라고 생각합니다.
# 최소 스패닝 트리를 만드는 방법을 알고있고, 어떻게 해야 길의 유지비의 합이
# 최소가 되도록 마을을 분할할지, "탐욕적인 사고방식"으로 떠올릴 수 있다면
# 쉽게 풀 수 있는 문제입니다.

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])

# kruskal
parent = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
        rank[root_b] += 1

costs = []
for edge in edges:
    a, b, c = edge
    a_root = find(a)
    b_root = find(b)
    if a_root == b_root:
        continue
    union(a, b)
    costs.append(c)

cost = sum(costs[:-1])
print(cost)