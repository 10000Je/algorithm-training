# no. 11404: 플로이드 (Gold IV)
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최소값
# 플로이드 와샬 알고리즘
# dist[n][m] = min(dist[n][m], dist[n][k]+dist[k][m]) 이라는 논리
# 이때 최단거리를 구해야 하므로 k가 1부터 n까지의 모든 도시인 경우를 탐색해야한다.
# 따라서 시간복잡도는 O(N^3)

import sys
from math import inf
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    dist[start][end] = min(dist[start][end], cost)

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for start in range(n):
        for end in range(n):
            dist[start][end] = min(dist[start][end], dist[start][k]+dist[k][end])

for i in range(n):
    for j in range(n):
        print(dist[i][j] if dist[i][j] != inf else 0, end=' ')
    print()