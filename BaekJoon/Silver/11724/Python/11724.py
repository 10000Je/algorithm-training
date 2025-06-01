import sys
from collections import deque

def bfs(graph, start):
    visited_vertices = {start}
    queue1 = deque([start])
    while queue1:
        cur_vertex = queue1.popleft()
        for near_vertex in graph[cur_vertex]:
            if near_vertex in visited_vertices:
                continue
            queue1.append(near_vertex)
            visited_vertices.add(near_vertex)
    return visited_vertices

n, m = map(int, sys.stdin.readline().split())
graph = {key: [] for key in range(1, n+1)}
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited_vertices = set()
for vertex in graph.keys():
    if vertex in visited_vertices:
        continue
    else:
        visited_vertices.update(bfs(graph, vertex))
        cnt += 1
print(cnt)