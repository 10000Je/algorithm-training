# no. 2638: 치즈 (Gold III)
# 실내온도의 공기와 접촉한 치즈 격자는 한 시간 후에 사라진다.
# 접촉의 기준(치즈 외부 공기와 접촉한 면이 2변 이상)
# 내부공기와 외부공기를 어떻게 구별하지?
# bfs or dfs로 가장자리부터 (0,0)부터 시작해서 치즈를 만날때마다 cnt를 증가시키고
# cnt가 2이상인 치즈블럭은 1시간 뒤에 삭제시키면 될거같다.

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

def dfs(cur_cell, visited_cells=None, cnt=None):
    if cnt == None: cnt = {}
    if visited_cells == None: visited_cells = set()
    visited_cells.add(cur_cell)
    row, col = cur_cell
    near_cells = ((row+1, col), (row, col+1), (row-1, col), (row, col-1))
    for near_cell in near_cells:
        n_row, n_col = near_cell
        if n_row < 0 or n_row >= n or n_col < 0 or n_col >= m: continue
        if near_cell in visited_cells: continue
        if space[n_row][n_col] == 1:
            if near_cell not in cnt:
                cnt[near_cell] = 1
            else:
                cnt[near_cell] += 1
        else:
            dfs(near_cell, visited_cells, cnt)
    return cnt

def isempty():
    for r in range(n):
        for c in range(m):
            if space[r][c] == 1:
                return False
    return True

time = 0
while not isempty():
    cells = dfs((0, 0))
    for cell, cnt in cells.items():
        if cnt >= 2:
            row, col = cell
            space[row][col] = 0
    time += 1

print(time)