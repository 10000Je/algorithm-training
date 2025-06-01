# no. 16236: 아기 상어 (Gold III)
# bfs (가장 가까운 먹을 수 있는 물고기의 거리를 재야하기 때문이다.)
# 빈칸이면 이동가능
# 해당 칸에 존재하는 물고기가 나보다 크면 이동불가
# 크기가 같으면 이동은 가능 먹을순 없음
# 크기가 작으면 이동과 동시에 먹어버림

# 최대 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아머글수 잇음?

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

def getloc():
    for row in range(n):
        for col in range(n):
            if space[row][col] == 9:
                space[row][col] = 0
                return (row, col)
    return None

def bfs(start, size):
    cur_queue = deque((start,))
    dist = {start: 0}
    edible = []
    while cur_queue:
        cur_cell = cur_queue.popleft()
        row, col = cur_cell
        near_cells = (
            (row-1, col), (row, col+1), (row+1, col), (row, col-1)
        )
        for near_cell in near_cells:
            n_row, n_col = near_cell
            if n_row < 0 or n_row >= n or n_col < 0 or n_col >= n:
                continue
            if near_cell in dist:
                continue
            if space[n_row][n_col] > size:
                continue
            cur_queue.append(near_cell)
            dist[near_cell] = dist[cur_cell] + 1
            if 0 < space[n_row][n_col] < size:
                edible.append((dist[near_cell], n_row, n_col))
    return edible

loc = getloc()
size = 2
edible = bfs(loc, size)
time = 0
ate_fish = 0

while edible:
    fish = min(edible, key=lambda x:(x[0], x[1], x[2]))
    row, col = fish[1], fish[2]
    space[row][col] = 0
    loc = (row, col)
    time += fish[0]
    if size == ate_fish+1:
        size += 1
        ate_fish = 0
    else:
        ate_fish += 1
    edible = bfs(loc, size)

print(time)