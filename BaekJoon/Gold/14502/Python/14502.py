import sys

n, m = map(int, sys.stdin.readline().split())
cur_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def dfs(start, graph, visited_cells=None):
    row, col = start
    if not visited_cells:
        visited_cells = {start}
    near_cells = [
        (row-1, col), (row, col+1), (row+1, col), (row, col-1)
    ]
    for near_cell in near_cells:
        if near_cell in visited_cells:
            continue
        near_row, near_col = near_cell
        if not (0 <= near_row < len(graph) and 0 <= near_col < len(graph[near_row])):
            continue
        if graph[near_row][near_col] != 0:
            continue
        graph[near_row][near_col] = 2
        visited_cells.add(near_cell)
        dfs(near_cell, graph, visited_cells)

virus_spots = {(row, col) for row in range(n) for col in range(m) if cur_map[row][col] == 2}
max_safearea = 0
for i in range(n*m):
    first_row, first_col = i//m, i%m
    if cur_map[first_row][first_col] != 0:
        continue
    for j in range(n*m):
        second_row, second_col = j//m, j%m
        if cur_map[second_row][second_col] != 0:
            continue
        for k in range(n*m):
            third_row, third_col = k//m, k%m
            if cur_map[third_row][third_col] != 0:
                continue
            if i==j or j == k or k == i:
                continue
            new_map = [cur_row.copy() for cur_row in cur_map]
            new_map[first_row][first_col] = 1
            new_map[second_row][second_col] = 1
            new_map[third_row][third_col] = 1
            for virus_spot in virus_spots:
                dfs(virus_spot, new_map)
            safe_area = 0
            for new_row in new_map:
                safe_area += new_row.count(0)
            max_safearea = max(max_safearea, safe_area)

print(max_safearea)
            