import sys
from collections import deque

def bfs_traverse(box):
    start_points = [(i, j) for i in range(len(box)) for j in range(len(box[i])) if box[i][j] == 1]
    visited_vertices = set(start_points)
    queue1 = deque(start_points)
    distance = {key: 0 for key in start_points}
    if not distance:
        return 0
    while queue1:
        cur_vertex = queue1.popleft()
        row, col = cur_vertex
        near_vertices = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]
        for near_vertex in near_vertices:
            near_row, near_col = near_vertex
            if near_vertex in visited_vertices:
                continue
            if near_row < 0 or near_row >= len(box):
                continue
            if near_col < 0 or near_col >= len(box[near_row]):
                continue
            if box[near_row][near_col] == -1:
                continue
            queue1.append(near_vertex)
            visited_vertices.add(near_vertex)
            distance[near_vertex] = distance[cur_vertex] + 1
            box[near_row][near_col] = 1
    return max(distance.values())

m, n = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
distance = bfs_traverse(box)
for row in box:
    for col in row:
        if not col:
            distance = -1
            break
print(distance)