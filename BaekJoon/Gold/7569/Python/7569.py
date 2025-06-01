import sys
from collections import deque

def bfs(farm):
    start = [(height, row, col) for height in range(len(farm)) for row in range(len(farm[height])) for col in range(len(farm[height][row])) if farm[height][row][col] == 1]
    queue1 = deque(start)
    distance = {key: 0 for key in start}
    for hgt, row, col in start: farm[hgt][row][col] = 1
    while queue1:
        cur_vertex = queue1.popleft()
        hgt, row, col = cur_vertex
        near_vertices = [
            (hgt, row-1, col), (hgt, row, col+1), (hgt, row+1, col), 
            (hgt, row, col-1), (hgt+1, row, col), (hgt-1, row, col)
        ]
        for near_vertex in near_vertices:
            near_hgt, near_row, near_col = near_vertex
            if near_hgt < 0 or near_hgt >= len(farm):
                continue
            if near_row < 0 or near_row >= len(farm[near_hgt]):
                continue
            if near_col < 0 or near_col >= len(farm[near_hgt][near_row]):
                continue
            if not farm[near_hgt][near_row][near_col]:    
                farm[near_hgt][near_row][near_col] = 1
                distance[near_vertex] = distance[cur_vertex] + 1
                queue1.append(near_vertex)
    return distance

m, n, h = map(int, sys.stdin.readline().split())
farm = [[[num for num in map(int, sys.stdin.readline().split())] for i in range(n)] for j in range(h)]

distance = bfs(farm)
day = max(distance.values()) if distance else -1
for height in range(len(farm)):
    for row in range(len(farm[height])):
        for col in range(len(farm[height][row])):
            if not farm[height][row][col]:
                day = -1
                break
        else:
            continue
        break
    else:
        continue
    break
print(day)
