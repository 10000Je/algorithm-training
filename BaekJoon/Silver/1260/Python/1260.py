import sys
from collections import deque

def dfs(graph, start, visited_vertices=set()):
    visited_vertices.add(start)
    print(start, end=' ')
    if start not in graph:
        return
    for adjacent_vertex in sorted(graph[start]):
        if adjacent_vertex in visited_vertices:
            continue
        dfs(graph, adjacent_vertex, visited_vertices)

def bfs(graph, start):
    queue1 = deque(); queue1.append(start)
    visited_vertices = set(); visited_vertices.add(start)
    while queue1:
        current_vertex = queue1.popleft()
        print(current_vertex, end=' ')
        if current_vertex not in graph:
            continue
        for adjacent_vertex in sorted(graph[current_vertex]):
            if adjacent_vertex in visited_vertices:
                continue
            queue1.append(adjacent_vertex)
            visited_vertices.add(adjacent_vertex)

n, m, v = map(int, sys.stdin.readline().split())
graph = {}
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

dfs(graph, v)
print('\n', end='')
bfs(graph, v)
print('\n', end='')

    