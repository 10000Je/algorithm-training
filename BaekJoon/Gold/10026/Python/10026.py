import sys
from collections import deque

def bfs(grid, start, color_blind=False):
    visited_vertices = {start}
    queue1 = deque([start])
    start_color = grid[start[0]][start[1]]
    while queue1:
        cur_vertex = queue1.popleft()
        row, col = cur_vertex
        near_vertices = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]
        for near_vertex in near_vertices:
            if near_vertex in visited_vertices:
                continue
            near_row, near_col = near_vertex
            if near_row < 0 or near_row >= len(grid):
                continue
            if near_col < 0 or near_col >= len(grid[near_row]):
                continue
            if grid[near_row][near_col] == start_color or (color_blind and start_color in 'RG' and grid[near_row][near_col] in 'RG'):
                visited_vertices.add(near_vertex)
                queue1.append(near_vertex)
    return visited_vertices

n = int(sys.stdin.readline())
grid = [[char for char in sys.stdin.readline().rstrip()] for i in range(n)]

visited_cells = set()
cnt = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if (row, col) not in visited_cells:
            visited_cells.update(bfs(grid, (row, col)))
            cnt += 1
print(cnt, end=' ')

visited_cells.clear()
cnt = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if (row, col) not in visited_cells:
            visited_cells.update(bfs(grid, (row, col), color_blind=True))
            cnt += 1
print(cnt)