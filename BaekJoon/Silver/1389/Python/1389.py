# no. 1389: 케빈 베이컨의 6단계 법칙 (Silver I)
import sys
from collections import deque

def bfs(graph, vertex):
    distance = dict(); distance[vertex] = 0
    if vertex not in graph:
        return distance
    queue1 = deque(); queue1.append(vertex)
    visited_vertices = set(); visited_vertices.add(vertex)
    while queue1:
        current_vertex = queue1.popleft()
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex in visited_vertices:
                continue
            queue1.append(adjacent_vertex)
            visited_vertices.add(adjacent_vertex)
            distance[adjacent_vertex] = distance[current_vertex] + 1
    return distance


n, m = map(int, sys.stdin.readline().split())
graph = dict()
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

minCabinBacon = None
for vertex in graph.keys():
    distance = bfs(graph, vertex)
    cabin_bacon = (vertex, sum(distance.values()))
    if not minCabinBacon or cabin_bacon[1] < minCabinBacon[1]:
        minCabinBacon = cabin_bacon
    elif cabin_bacon[1] == minCabinBacon[1] and cabin_bacon[0] < minCabinBacon[0]:
        minCabinBacon = cabin_bacon
print(minCabinBacon[0])

