import sys
from collections import deque

def bfs(graph, start, end):
    queue1 = deque([i for i in range(n) if graph[start][i]])
    visited_cells = {i for i in range(n) if graph[start][i]}
    while queue1:
        cur_cell = queue1.popleft()
        if cur_cell == end:
            return True
        near_cells = [i for i in range(n) if graph[cur_cell][i] and i not in visited_cells]
        for near_cell in near_cells:
            visited_cells.add(near_cell)
            queue1.append(near_cell)
    return False
    
n = int(sys.stdin.readline())
graph = [[i for i in map(int, sys.stdin.readline().split())] for i in range(n)]
memo = [[0 for i in range(n)] for i in range(n)]
for row in range(n):
    for col in range(n):
        if bfs(graph, row, col):
            memo[row][col] = 1
        else:
            memo[row][col] = 0
for row in memo:
    print(' '.join(map(str, row)))