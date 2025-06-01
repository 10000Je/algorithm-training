import sys
from collections import deque

def bfs(graph, start):
    distance = {start:0}
    visited_vertices = {start}
    queue1 = deque([start])
    while queue1:
        cur_vertex = queue1.popleft()
        row, col = cur_vertex
        near_vertices = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]
        for near_vertex in near_vertices:
            if near_vertex in visited_vertices:
                continue
            near_row, near_col = near_vertex
            if near_row < 0 or near_row >= len(graph):
                continue
            if near_col < 0 or near_col >= len(graph[near_row]):
                continue
            if not graph[near_row][near_col]:
                continue
            distance[near_vertex] = distance[cur_vertex] + 1
            visited_vertices.add(near_vertex)
            queue1.append(near_vertex)
    return distance

n, m = map(int, sys.stdin.readline().split())
map1 = [[int(char) for char in sys.stdin.readline().split()] for i in range(n)]
end_loc = [(row, col) for row in range(len(map1)) for col in range(len(map1[row])) if map1[row][col] == 2][0]
memo = bfs(map1, end_loc)
for row in range(len(map1)):
    for col in range(len(map1[row])):
        if (row, col) in memo:
            map1[row][col] = memo[(row, col)]
        else:
            if map1[row][col]:
                map1[row][col] = -1

for row in map1:
    print(' '.join(map(str, row)))