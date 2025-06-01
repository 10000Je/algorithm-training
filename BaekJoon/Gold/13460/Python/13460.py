# no. 13460: 구슬 탈출 2
# 상하좌우로 기울이기가 핵심
# 기울이는건 더이상 구슬이 움직이지 않을때까지, 즉, 기울이면 기울인 쪽으로 구슬이
# 갈 수 있는 만큼 움직여야함
# 이때 파란구슬이 구멍에 빠지면 이 경우는 실패로 간주해야함
# 빨간 구슬과 파란 구슬은 같은 칸에 존재할 수 없음
# 빨간 구슬과 파란 구슬이 동시에 구멍에서 빠져도 실패
# 벽의 위치와 구멍의 위치는 변하지 않음
# backtracking.

# 풀고나서 리뷰
# 이문제 bfs로도 풀 수 있다고 한다.
# 알고리즘 분류를 안보고 풀어서 백트래킹으로 풀었는데
# 왜 bfs 해법을 보지 못했을까?
# ... 일단 depth, 즉 경로의 길이가 10 이상인 경우를 고려하지 않아도 되서
# 시간복잡도에 문제가 없어서 백트래킹으로만 풀 생각이였던 것 같다
# bfs에 대한 이 편견때문에 "기울이기"를 이동으로 볼 생각 자체를 못했다
# 구현이 전부였던 문제, 기울이기 구현이 개빡세다 진짜

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
board = tuple(tuple(input().rstrip()) for _ in range(n))

red = blue = None
for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            red = (r, c)
        if board[r][c] == 'B':
            blue = (r, c)

# direction -> UP, DOWN, LEFT, RIGHT
def tilt(loc, direction):
    r, c = loc
    if board[r][c] == 'O':
        return (r, c)
    if direction == 'UP':
        if board[r-1][c] == '#':
            return (r, c)
        return tilt((r-1, c), 'UP')
    if direction == 'DOWN':
        if board[r+1][c] == '#':
            return (r, c)
        return tilt((r+1, c), 'DOWN')
    if direction == 'LEFT':
        if board[r][c-1] == '#':
            return (r, c)
        return tilt((r, c-1), 'LEFT')
    if direction == 'RIGHT':
        if board[r][c+1] == '#':
            return (r, c)
        return tilt((r, c+1), 'RIGHT')


def dfs(red, blue, depth=0, cnt=[11]):
    if depth > 10:
        return # 10번 초과로 움직였다면 실패
    if board[blue[0]][blue[1]] == 'O':
        return # 파란 공이 먼저 또는 동시에 밖으로 나온 경우 실패
    if board[red[0]][red[1]] == 'O':
        cnt[0] = min(cnt[0], depth)
        return
    # 위로 기울이기
    next_red = tilt(red, "UP")
    next_blue = tilt(blue, "UP")
    # 위로 기울였는데, 둘이 같은 지점으로 간다면 (단, 구멍으로 나온경우는 제외)
    if next_red == next_blue and board[next_red[0]][next_red[1]] != 'O':
        if red[0] < blue[0]: # 원래 빨간 공이 파란 공보다 위에 있었던 경우
            r, c = next_blue
            next_blue = (r+1, c)
        if red[0] > blue[0]:
            r, c = next_red
            next_red = (r+1, c)
    dfs(next_red, next_blue, depth+1, cnt)
    # 아래로 기울이기
    next_red = tilt(red, "DOWN")
    next_blue = tilt(blue, "DOWN")
    # 아래로 기울였는데, 둘이 같은 지점으로 간다면 (단, 구멍으로 나온경우는 제외)
    if next_red == next_blue and board[next_red[0]][next_red[1]] != 'O':
        if red[0] < blue[0]: # 원래 파란 공이 빨간 공보다 아래에 있었던 경우
            r, c = next_red
            next_red = (r-1, c)
        if red[0] > blue[0]:
            r, c = next_blue
            next_blue = (r-1, c)
    dfs(next_red, next_blue, depth+1, cnt)
    # 좌로 기울이기
    next_red = tilt(red, "LEFT")
    next_blue = tilt(blue, "LEFT")
    # 좌로 기울였는데, 둘이 같은 지점으로 간다면 (단, 구멍으로 나온경우는 제외)
    if next_red == next_blue and board[next_red[0]][next_red[1]] != 'O':
        if red[1] < blue[1]: # 원래 빨간 공이 파랑 공보다 왼쪽에 있었던 경우
            r, c = next_blue
            next_blue = (r, c+1)
        if red[1] > blue[1]:
            r, c = next_red
            next_red = (r, c+1)
    dfs(next_red, next_blue, depth+1, cnt)
    # 우로 기울이기
    next_red = tilt(red, "RIGHT")
    next_blue = tilt(blue, "RIGHT")
    # 우로 기울였는데, 둘이 같은 지점으로 간다면 (단, 구멍으로 나온경우는 제외)
    if next_red == next_blue and board[next_red[0]][next_red[1]] != 'O':
        if red[1] < blue[1]: # 원래 파랑 공이 빨간 공보다 오른쪽에 있었던 경우
            r, c = next_red
            next_red = (r, c-1)
        if red[1] > blue[1]:
            r, c = next_blue
            next_blue = (r, c-1)
    dfs(next_red, next_blue, depth+1, cnt)
    return cnt[0]

cnt = dfs(red, blue)
if cnt == 11:
    print(-1)
else:
    print(cnt)