import sys
from collections import deque

def bfs(shortcuts):
    visited_cells = {1}
    dist = {1:0}
    queue1 = deque([1])
    while queue1:
        cur_cell = queue1.popleft()
        near_cells = [i for i in range(cur_cell+1, cur_cell+7) if i <= 100 and i not in visited_cells]
        for near_cell in near_cells:
            if near_cell in shortcuts:
                if shortcuts[near_cell] in visited_cells:
                    continue
                else:
                    near_cell = shortcuts[near_cell]
            dist[near_cell] = dist[cur_cell] + 1
            queue1.append(near_cell)
            visited_cells.add(near_cell)
    return dist[100]

n, m = map(int, sys.stdin.readline().split())
shortcuts = {}
for i in range(n+m):
    start, end = map(int, sys.stdin.readline().split())
    shortcuts[start] = end
    
print(bfs(shortcuts))