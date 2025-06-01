# no. 20040: 사이클 게임 (Gold IV)
# 평면 상의 점 n개가 주어지며, 이 중 어느 세 점도 일직선 위에 놓이지 않는다.
# 두 점을 선택해서 이를 연결하는 선분을 긋는데, 이전에 그린 선분은
# 다시 그을 수 없으면, 다른 선분을 교차하는 것은 상관없다. 사이클을 완성하면
# 몇번째 선분을 그었을때 사이클을 완성했는지 출력해야하며 만약 모든
# 선분을 그었음에도 사이클을 완성하지 못했다면 0을 출력해야한다

# 체감 난이도: Gold V
# 분리집합을 union-find 알고리즘을 통해 구현하는 방법을 안다면
# 사실 난이도 Gold V를 줘도 되는 문제

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
lines = tuple(tuple(map(int, input().split())) for _ in range(m))

parent = [i for i in range(n)]
rank = [0 for _ in range(n)]

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
        parent[root_b] = root_a
        rank[root_a] += 1

no = 0
for i in range(m):
    a, b = lines[i]
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        no = i+1
        break
    union(root_a, root_b)

print(no)