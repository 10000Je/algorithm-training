# no. 1697: 숨바꼭질 (Silver I)
from collections import deque

def bfs(start, end):
    queue1 = deque(); queue1.append(start)
    visited_vertices = set(); visited_vertices.add(start)
    distance = {}; distance[start] = 0
    while queue1:
        current_vertex = queue1.popleft()
        adjacent_vertices = []
        if current_vertex * 2 <= 100_000:
            adjacent_vertices.append(current_vertex * 2)
        if current_vertex + 1 <= 100_000:
            adjacent_vertices.append(current_vertex + 1)
        if current_vertex - 1 >= 0:
            adjacent_vertices.append(current_vertex - 1)
        for adjacent_vertex in adjacent_vertices:
            if adjacent_vertex in visited_vertices:
                continue
            distance[adjacent_vertex] = distance[current_vertex] + 1
            visited_vertices.add(adjacent_vertex)
            queue1.append(adjacent_vertex)
    return distance[end]

n, k = map(int, input().split())
print(bfs(n, k))

