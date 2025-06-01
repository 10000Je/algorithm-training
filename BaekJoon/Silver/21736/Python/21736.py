import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
campus = [[char for char in sys.stdin.readline().rstrip()] for _ in range(n)]
loc = None
for row in range(len(campus)):
    for col in range(len(campus[row])):
        if campus[row][col] == 'I':
            loc = (row, col)
            break
    else:
        continue
    break
queue = deque([loc])
visited_space = {loc}
cnt = 0
while queue:
    cur_space = queue.popleft()
    row, col = cur_space
    if campus[row][col] == 'P':
        cnt += 1
    near_spaces = [
        (row+1, col), (row, col+1), (row-1, col), (row, col-1)
    ]
    for near_space in near_spaces:
        if near_space in visited_space: 
            continue
        n_row, n_col = near_space
        if not (0 <= n_row < len(campus) and 0 <= n_col < len(campus[n_row])): 
            continue
        if campus[n_row][n_col] == 'X': 
            continue
        visited_space.add(near_space)
        queue.append(near_space)
print(cnt or 'TT')