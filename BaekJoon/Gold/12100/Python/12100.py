# no. 12100: 2048 (Easy)
# 구현, 시뮬레이션, 백트래킹
# 풀고나서 후기:
# move 구현이 정말 지치는 작업이였다
# 그래도 한번만에 구현에 성공해서 다행이지 막 틀리고 ㄱㅈㄹ 났으면 접었을지도
# 난이도, 알고리즘 힌트 다 안보고 풀어서 뿌듯하긴 하다

from sys import stdin
input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# direction -> U, D, L, R
# return -> board(after movement)
def move(board, direction):
    if direction == 'U':
        new_board = [board[i][:] for i in range(n)]
        for c in range(n): # 위로 이동시켰으므로, 열마다 반복
            unionstate = [0 for _ in range(n)]
            for r in range(n): # 해당 열에서 숫자를 발견했을 경우
                if new_board[r][c]:
                    cur_r = r-1
                    while True:
                        if cur_r == -1: # 만약 이동시키는 경로내에 다른 합체가능한 숫자가 존재하지 않았다면
                            new_board[0][c] = new_board[r][c]
                            if r != 0:
                                new_board[r][c] = 0
                            break
                        elif new_board[cur_r][c] == 0: 
                            cur_r -= 1
                        elif new_board[cur_r][c] == new_board[r][c] and unionstate[cur_r] == 0: # 만약, 두 숫자가 같고, 합쳐진 적이 없다면
                            new_board[r][c] = 0
                            new_board[cur_r][c] *= 2
                            unionstate[cur_r] = 1
                            break
                        else: # 또는 숫자가 다르거나, 이미 합쳐진 적이 있다면
                            new_board[cur_r+1][c] = new_board[r][c]
                            if r != cur_r+1:
                                new_board[r][c] = 0
                            break
        return new_board
    if direction == 'D':
        new_board = [board[i][:] for i in range(n)]
        for c in range(n): # 아래로 이동시켰으므로, 열마다 반복
            unionstate = [0 for _ in range(n)]
            for r in reversed(range(n)): # 해당 열에서 숫자를 발견했을 경우
                if new_board[r][c]:
                    cur_r = r+1
                    while True:
                        if cur_r == n: # 만약 이동시키는 경로내에 다른 합체가능한 숫자가 존재하지 않았다면
                            new_board[n-1][c] = new_board[r][c]
                            if r != n-1:
                                new_board[r][c] = 0
                            break
                        elif new_board[cur_r][c] == 0: 
                            cur_r += 1
                        elif new_board[cur_r][c] == new_board[r][c] and unionstate[cur_r] == 0: # 만약, 두 숫자가 같고, 합쳐진 적이 없다면
                            new_board[r][c] = 0
                            new_board[cur_r][c] *= 2
                            unionstate[cur_r] = 1
                            break
                        else: # 또는 숫자가 다르거나, 이미 합쳐진 적이 있다면
                            new_board[cur_r-1][c] = new_board[r][c]
                            if r != cur_r-1:
                                new_board[r][c] = 0
                            break
        return new_board
    if direction == 'L':
        new_board = [board[i][:] for i in range(n)]
        for r in range(n): # 왼쪽으로 이동시켰으므로, 행마다 반복
            unionstate = [0 for _ in range(n)]
            for c in range(n): # 해당 행에서 숫자를 발견했을 경우
                if new_board[r][c]:
                    cur_c = c-1
                    while True:
                        if cur_c == -1: # 만약 이동시키는 경로내에 다른 합체가능한 숫자가 존재하지 않았다면
                            new_board[r][0] = new_board[r][c]
                            if c != 0:
                                new_board[r][c] = 0
                            break
                        elif new_board[r][cur_c] == 0: 
                            cur_c -= 1
                        elif new_board[r][cur_c] == new_board[r][c] and unionstate[cur_c] == 0: # 만약, 두 숫자가 같고, 합쳐진 적이 없다면
                            new_board[r][c] = 0
                            new_board[r][cur_c] *= 2
                            unionstate[cur_c] = 1
                            break
                        else: # 또는 숫자가 다르거나, 이미 합쳐진 적이 있다면
                            new_board[r][cur_c+1] = new_board[r][c]
                            if c != cur_c+1:
                                new_board[r][c] = 0
                            break
        return new_board
    if direction == 'R':
        new_board = [board[i][:] for i in range(n)]
        for r in range(n): # 오른쪽으로 이동시켰으므로, 행마다 반복
            unionstate = [0 for _ in range(n)]
            for c in reversed(range(n)): # 해당 행에서 숫자를 발견했을 경우
                if new_board[r][c]:
                    cur_c = c+1
                    while True:
                        if cur_c == n: # 만약 이동시키는 경로내에 다른 합체가능한 숫자가 존재하지 않았다면
                            new_board[r][n-1] = new_board[r][c]
                            if c != n-1:
                                new_board[r][c] = 0
                            break
                        elif new_board[r][cur_c] == 0: 
                            cur_c += 1
                        elif new_board[r][cur_c] == new_board[r][c] and unionstate[cur_c] == 0: # 만약, 두 숫자가 같고, 합쳐진 적이 없다면
                            new_board[r][c] = 0
                            new_board[r][cur_c] *= 2
                            unionstate[cur_c] = 1
                            break
                        else: # 또는 숫자가 다르거나, 이미 합쳐진 적이 있다면
                            new_board[r][cur_c-1] = new_board[r][c]
                            if c != cur_c-1:
                                new_board[r][c] = 0
                            break
        return new_board
                            
# return -> block maximum size
def backtracking(cur_board, depth=0, max_size=None):
    if max_size == None: max_size = [0]
    if depth == 5:
        max_size[0] = max(max(map(max, cur_board)), max_size[0])
        return max_size[0]
    backtracking(move(cur_board, 'U'), depth+1, max_size)
    backtracking(move(cur_board, 'D'), depth+1, max_size)
    backtracking(move(cur_board, 'L'), depth+1, max_size)
    backtracking(move(cur_board, 'R'), depth+1, max_size)
    return max_size[0]

max_size = backtracking(board)
print(max_size)