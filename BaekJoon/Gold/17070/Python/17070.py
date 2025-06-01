# no. 17070: 파이프 옮기기 1
# 파이프를 옮길 지정된 위치로 옮길 수 있는 경우의 수를 구하라
# 백트래킹...
# 가로인경우 가로로 밀거나, 밀면서 45도 회전
# 세로인경우 세로로 밀거나, 밀면서 45도 회전
# 대각선인경우 그대로 밀거나, 밀면서 45도 회전

# 참고로 이 문제는 dp로도 풀수있으나, 이 문제의 조건은 백트래킹으로도 풀리는
# 문제이기 때문에 일단 이 해답만 남겨놓으려고 한다. 제출목록에 40ms 해법이 dp이다.

from sys import stdin
input = stdin.readline

n = int(input())
home = tuple(tuple(map(int, input().split())) for _ in range(n))

def dfs(r=0, c=1, state=0, cnt=None):
    if cnt == None: cnt = [0]
    if r == n-1 and c == n-1:
        cnt[0] += 1
        return
    if state == 0:
        if 0 <= c+1 < n and home[r][c+1] != 1:
            dfs(r, c+1, 0, cnt)
        if 0 <= r+1 < n and 0 <= c+1 < n and home[r+1][c] != 1 and home[r][c+1] != 1 and home[r+1][c+1] != 1:
            dfs(r+1, c+1, 2, cnt)
    if state == 1:
        if 0 <= r+1 < n and home[r+1][c] != 1:
            dfs(r+1, c, 1, cnt)
        if 0 <= r+1 < n and 0 <= c+1 < n and home[r+1][c] != 1 and home[r][c+1] != 1 and home[r+1][c+1] != 1:
            dfs(r+1, c+1, 2, cnt)
    if state == 2:
        if 0 <= r+1 < n and 0 <= c+1 < n and home[r+1][c] != 1 and home[r][c+1] != 1 and home[r+1][c+1] != 1:
            dfs(r+1, c+1, 2, cnt)
        if 0 <= r+1 < n and home[r+1][c] != 1:
            dfs(r+1, c, 1, cnt)
        if 0 <= c+1 < n and home[r][c+1] != 1:
            dfs(r, c+1, 0, cnt)
    return cnt[0]

print(dfs())