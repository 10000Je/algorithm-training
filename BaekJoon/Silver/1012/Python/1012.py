import sys
from collections import deque

def bfs_traverse(farm, row, column):
    queue1 = deque()
    queue1.append((row, column))
    visited_cells = set()
    visited_cells.add((row, column))
    while queue1:
        current_cell = queue1.popleft()
        adjacent_cells = [
            (current_cell[0]+1, current_cell[1]),
            (current_cell[0], current_cell[1]+1),
            (current_cell[0]-1, current_cell[1]),
            (current_cell[0], current_cell[1]-1)
            ]
        for adjacent_cell in adjacent_cells:
            if adjacent_cell in visited_cells:
                continue
            if adjacent_cell[0] < 0 or adjacent_cell[0] >= len(farm):
                continue
            if adjacent_cell[1] < 0 or adjacent_cell[1] >= len(farm[adjacent_cell[0]]):
                continue
            if not farm[adjacent_cell[0]][adjacent_cell[1]]:
                continue
            farm[adjacent_cell[0]][adjacent_cell[1]] = 0
            queue1.append(adjacent_cell)
            visited_cells.add(adjacent_cell)

t = int(sys.stdin.readline())
for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[0 for i in range(m)] for i in range(n)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        farm[y][x] = 1
    count = 0
    for row in range(len(farm)):
        for column in range(len(farm[0])):
            if farm[row][column]:
                bfs_traverse(farm, row, column)
                count += 1
    print(count)
