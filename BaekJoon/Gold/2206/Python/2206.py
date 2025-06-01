# no. 2206: 벽 부수고 이동하기 (Gold III)

# 일단 벽만 부수는거 없으면 기본적인 bfs 최단거리 문제인데...
# 벽을 아주그냥 시원하게 부셔버린다고 합니다..
# 벽의 개수는 최대 백만개 정도 되니까 벽을 한개씩 없애고 매번 bfs 돌리면 무조건 시간초과임

# 만약 벽을 부순 경우 최단거리가 된다면
# 최단거리는 시작점 - 벽위치 + 벽위치 - 도착점 이 될것이다.
# 최단거리안에 무조건 부순 벽의 위치가 존재할 것이기 때문이다.

# 즉, 최단거리는 시작점-도착점
# 즉, 시작점-벽 + 벽-도착점 조합중 최소값이 될것이다.

# 시작점으로부터 모든 "벽" 까지의 거리들을 구하고
# 도착점으로부터 모든 "벽" 까지의 거리들을 구하고
# 벽을 부수는 이동거리들+안부순 경우의 최단거리 중 최소값이
# 문제의 답이다.

import sys
import math
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[int(char) for char in input().rstrip()] for _ in range(n)]

def bfs(start, end=None):
    dist = {start: 1}
    dist_walls = {}
    cur_queue = deque([start])
    while cur_queue:
        cur_cell = cur_queue.popleft()
        row, col = cur_cell
        near_cells = [
            (row+1, col), (row, col+1), (row-1, col), (row, col-1)
        ]
        for near_cell in near_cells:
            n_row, n_col = near_cell
            if not (0<=n_row<n and 0<=n_col<m):
                continue
            if graph[n_row][n_col] == 1:
                if (n_row, n_col) not in dist_walls:
                    dist_walls[near_cell] = dist[cur_cell]+1
                else:
                    dist_walls[near_cell] = min(dist_walls[near_cell], dist[cur_cell]+1)
            else:
                if near_cell in dist:
                    continue
                dist[near_cell] = dist[cur_cell]+1
                cur_queue.append(near_cell)
    if end == None:
        return dist_walls
    else:
        if end in dist:
            return dist[end]
        else:
            return math.inf

dist_start = bfs((0, 0))
dist_end = bfs((n-1, m-1))
breakable_walls = set()
for key in dist_start.keys():
    if key in dist_end:
        breakable_walls.add(key)
nobreaking_dist = bfs((0, 0), (n-1, m-1))

if not breakable_walls and nobreaking_dist==math.inf:
    print(-1)
else:
    min_dist = nobreaking_dist
    for key in breakable_walls:
        min_dist = min(min_dist, dist_start[key]+dist_end[key]-1)
    print(min_dist)