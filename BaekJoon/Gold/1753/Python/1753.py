import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
k = int(input())
graph = {i: dict() for i in range(1, n+1)}
for _ in range(e):
    u, v, w = map(int, input().split())
    if v not in graph[u]:
        graph[u][v] = w
    else:
        graph[u][v] = min(graph[u][v], w)

def dijkstra(start, graph, visited_vertices=set()):
    dist = {start: 0}
    unvisited_vertices = [(dist[start], start)]
    while unvisited_vertices:
        cur_vertex = heapq.heappop(unvisited_vertices)[1]
        if cur_vertex in visited_vertices:
            continue
        visited_vertices.add(cur_vertex)
        for near_vertex, weight in graph[cur_vertex].items():
            if near_vertex in visited_vertices:
                continue
            if near_vertex not in dist or dist[cur_vertex] + weight < dist[near_vertex]:
                dist[near_vertex] = dist[cur_vertex] + weight
                heapq.heappush(unvisited_vertices, (dist[near_vertex], near_vertex))
    return dist

dist = dijkstra(k, graph)
for i in range(1, n+1):
    if i not in dist:
        print('INF')
    else:
        print(dist[i])