# no. 17144: 미세먼지 안녕! (Gold IV)
# 미세먼지의 확산, 공기청정기의 작동만 구현하면 쉬운문제

from sys import stdin
input = stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

def spreading():
    dusts = [(row, col, room[row][col]) for row in range(r) for col in range(c) if room[row][col] > 0]
    for dust in dusts:
        row, col, amount = dust
        near_cells = [
            (row+1, col), (row, col+1), (row-1, col), (row, col-1)
        ]
        cnt = 0
        for near_cell in near_cells:
            n_row, n_col = near_cell
            if n_row < 0 or n_row >= r or n_col < 0 or n_col >= c:
                continue
            if room[n_row][n_col] == -1:
                continue
            cnt += 1
            room[n_row][n_col] += amount//5
        room[row][col] -= (amount//5)*cnt

def purifying():
    purifier = [row for row in range(r) if room[row][0] == -1]
    up, down = purifier
    for i in range(up-1, -1, -1):
        if room[i+1][0] != -1:
            room[i+1][0] = room[i][0]
        room[i][0] = 0
    for i in range(1, c):
        room[0][i-1] = room[0][i]
        room[0][i] = 0
    for i in range(1, up+1):
        room[i-1][c-1] = room[i][c-1]
        room[i][c-1] = 0
    for i in range(c-2, 0, -1):
        room[up][i+1] = room[up][i]
        room[up][i] = 0
    for i in range(down+1, r):
        if room[i-1][0] != -1:
            room[i-1][0] = room[i][0]
        room[i][0] = 0
    for i in range(1, c):
        room[r-1][i-1] = room[r-1][i]
        room[r-1][i] = 0
    for i in range(r-2, down-1, -1):
        room[i+1][c-1] = room[i][c-1]
        room[i][c-1] = 0
    for i in range(c-2, 0, -1):
        room[down][i+1] = room[down][i]
        room[down][i] = 0

for _ in range(t):
    spreading()
    purifying()

dust = 0
for row in range(r):
    for col in range(c):
        if room[row][col] > 0:
            dust += room[row][col]    
print(dust)