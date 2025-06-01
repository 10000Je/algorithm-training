# no. 1238: 파티 (Gold III)
# n개의 숫자로 구분된 마을에 한명의 학생이 각각 살고있음
# x번 마을에 모여서 파티를 벌이기로 함
# 마을 사이에는 m개의 도로(간선)이 있고 i번째 도로는 ti시간을 소비함(가중치 존재)
# 모든 학생들은 다시 그들의 마을로 돌아와야함
# 모든 학생은 자신의 마을로부터 최단거리로 왔다 간다.(다만 도로가 단방향이라 가는길과
# 오는길이 다를 수 있다.)
# 다행히 파티는 한번만 하나보다. x가 주어진다.
# x로부터 모든 마을의 거리는 쉽게 구할 수 있을거 같다.

# 모든 마을로부터 x까지의 각 거리는 어떻게 구할까?
# 최적화된 다익스트라 알고리즘 O(ElogV)
# 모든 정점에서 실행해야 함 O(EVlogV) -> 가능

import sys
import heapq
from math import inf
input = sys.stdin.readline

n, m, x = map(int, input().split())

villages = {i: {} for i in range(1, n+1)}
for _ in range(m):
    start, end, weight = map(int, input().split())
    villages[start][end] = weight

def dijkstra(start, end=None):
    dist = {i: inf for i in range(1, n+1)}
    dist[start] = 0
    unvisited_village = [(0, start)]
    visited_village = set()
    while unvisited_village:
        cur_village = heapq.heappop(unvisited_village)[1]
        if cur_village == end:
            return dist[end]
        if cur_village in visited_village:
            continue
        visited_village.add(cur_village)
        for near_village, weight in villages[cur_village].items():
            dist[near_village] = min(dist[near_village], dist[cur_village]+weight)
            heapq.heappush(unvisited_village, (dist[near_village], near_village))
    return dist

dist_from_x = dijkstra(x)
max_dist = -inf
for i in range(1, n+1):
    dist_to_x = dijkstra(i, x)
    max_dist = max(max_dist, dist_from_x[i]+dist_to_x)

print(max_dist)