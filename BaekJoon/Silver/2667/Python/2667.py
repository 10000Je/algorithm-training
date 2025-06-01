import sys
from collections import deque

def bfs(graph, start):
    queue1 = deque(); queue1.append(start)
    graph[start[0]][start[1]] = 0
    cnt = 1
    while queue1:
        cur_vertex = queue1.popleft()
        row, col = cur_vertex
        near_vertices = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]
        for near_vertex in near_vertices:
            near_row, near_col = near_vertex
            if near_row < 0 or near_row >= len(graph):
                continue
            if near_col < 0 or near_col >= len(graph[near_row]):
                continue
            if graph[near_row][near_col]:
                graph[near_row][near_col] = 0
                queue1.append(near_vertex)
                cnt += 1
    return cnt

n = int(sys.stdin.readline())
map1 = [[int(char) for char in sys.stdin.readline().rstrip()] for i in range(n)]
groups = []
for row in range(len(map1)):
    for col in range(len(map1[row])):
        if map1[row][col]:
            cnt = bfs(map1, (row, col))
            groups.append(cnt)
groups.sort()
print(len(groups))
for cnt in groups:
    print(cnt)
