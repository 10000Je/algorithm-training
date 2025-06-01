# no. 17143: 낚시왕 (Gold I)
# 상어의 이동을 구현하는 것이 문제의 핵심이다.
# 이동시 경계를 벗어나지 않는다면
# r-s or r+s or c-s or c+s
# 이동시 경계를 벗어난다면
# 맨 끝점에서 맨 끝점으로 가는데 r-1번 이동해야한다
# 편도로 이동하는데 r-1번 걸리므로, (s-c) 를 (r-1)로 나눈 몫만큼 방향이 바뀐다.
# 동시에 바뀐 방향에서 (s-c) 를 (r-1)로 나눈 나머지만큼 이동하게 된다
# up, down, left, right 4개의 함수를 구현하여 작성하면 가독성이 좋을 것 같다

# 후기
# 체감 난이도: Gold I
# 구현존나 빡세다 진짜..

from sys import stdin
input = stdin.readline

r, c, m = map(int, input().split())
board = [[None for _ in range(c)] for _ in range(r)]

for _ in range(m):
    i, j, s, d, z = map(int, input().split())
    board[i-1][j-1] = (s, d, z)
    
def catch(loc):
    for row in range(r):
        if board[row][loc] != None:
            return (row, loc)
    return None

def find():
    locs = []
    for row in range(r):
        for col in range(c):
            if board[row][col] != None:
                locs.append((row, col))
    return locs

def up(row, speed):
    if speed <= row:
        return (row-speed, 1)
    else:
        mov_cnt = (speed-row) % (r-1)
        dir_cnt = (speed-row) // (r-1)
        dir_cnt = dir_cnt + 1
        if dir_cnt % 2 == 0:
            return ((r-1)-mov_cnt, 1)
        else:
            return (mov_cnt, 2)

def down(row, speed):
    if row+speed <= r-1:
        return (row+speed, 2)
    else:
        mov_cnt = (speed-((r-1)-row)) % (r-1)
        dir_cnt = (speed-((r-1)-row)) // (r-1)
        dir_cnt = dir_cnt + 1
        if dir_cnt % 2 == 0:
            return (mov_cnt, 2)
        else:
            return ((r-1)-mov_cnt, 1)

def left(col, speed):
    if speed <= col:
        return (col-speed, 4)
    else:
        mov_cnt = (speed-col) % (c-1)
        dir_cnt = (speed-col) // (c-1)
        dir_cnt = dir_cnt + 1
        if dir_cnt % 2 == 0:
            return ((c-1)-mov_cnt, 4)
        else:
            return (mov_cnt, 3)

def right(col, speed):
    if col+speed <= c-1:
        return (col+speed, 3)
    else:
        mov_cnt = (speed-((c-1)-col)) % (c-1)
        dir_cnt = (speed-((c-1)-col)) // (c-1)
        dir_cnt = dir_cnt + 1
        if dir_cnt % 2 == 0:
            return (mov_cnt, 3)
        else:
            return ((c-1)-mov_cnt, 4)

size_sum = 0
for col in range(c):
    loc = catch(col)
    if loc != None:
        row, col = loc
        speed, direction, size = board[row][col]
        board[row][col] = None
        size_sum += size
    shark_locs = find()
    new_board = [[None for _ in range(c)] for _ in range(r)]
    for loc in shark_locs:
        row, col = loc
        speed, direction, size = board[row][col]
        if direction == 1:
            row, direction = up(row, speed)
        elif direction == 2:
            row, direction = down(row, speed)
        elif direction == 3:
            col, direction = right(col, speed)
        elif direction == 4:
            col, direction = left(col, speed)
        if new_board[row][col] == None or new_board[row][col][2] < size:
            new_board[row][col] = (speed, direction, size)
    board = new_board

print(size_sum)