# no. 1504: 특정한 최단 경로 (Gold IV)
# 방향성이 없는 그래프가 주어진다.
# 1번 정점에서 N번 정점까지의 최단거리를 구하자
# 단 그 최단경로는 두 정점 v1, v2 를 무조건 지나는 최단경로 여야한다.
# 1-v1 까지의 최단경로, v1-v2 까지의 최단경로, v2-n까지의 최단경로가 답이되지 않나?

import heapq
from sys import stdin
from math import inf
input = stdin.readline

n, e = map(int, input().split())
graph = {i: {} for i in range(1, n+1)}

for _ in range(e):
    a, b, c = map(int, input().split())
    if b not in graph[a]:
        graph[a][b] = c
        graph[b][a] = c
    else:
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    unvisited_vertices = [(0, start)]
    visited_vertices = set()
    dist = {i: inf for i in range(1, n+1)}
    dist[start] = 0
    while unvisited_vertices:
        cur_vertex = heapq.heappop(unvisited_vertices)[1]
        if cur_vertex == end:
            return dist[end]
        if cur_vertex in visited_vertices:
            continue
        visited_vertices.add(cur_vertex)
        for near_vertex, weight in graph[cur_vertex].items():
            if near_vertex in visited_vertices:
                continue
            dist[near_vertex] = min(dist[near_vertex], dist[cur_vertex]+weight)
            heapq.heappush(unvisited_vertices, (dist[near_vertex], near_vertex))
    return dist[end]

d1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
d2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if d1 < d2:
    print(d1)
elif d1 > d2:
    print(d2)
elif d1 == d2 and d1 != inf:
    print(d1)
else:
    print(-1)