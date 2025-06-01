# no. 14938: 서강그라운드 (Gold IV)
# 한 정점에서 최단거리가 수색범위보다 작거나 같은 지점들의 아이템의 개수의 합을 구해라
# 가중치는 양수이다.
# 지역의 개수 n <= 100, 길의 개수 r <= 100
# 시간제한 1초 -> floyd-washal 사용가능 1_000_000...

from sys import stdin
input = stdin.readline
inf = 10**4

n, m, r = map(int, input().split())
items = tuple(map(int, input().split()))
dist = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    a, b = a-1, b-1
    dist[a][b] = dist[b][a] = l

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

max_items = 0
for i in range(n):
    cur_items = 0
    for j in range(n):
        if dist[i][j] <= m:
            cur_items += items[j]
    max_items = max(max_items, cur_items)

print(max_items)