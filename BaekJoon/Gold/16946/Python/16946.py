# no. 16946: 벽 부수고 이동하기 4 (Gold II)
# dfs/bfs 탐색 문제
# 벽을 부술때마다 dfs/bfs로 탐색을 진행하면 시간초과를 못피한다
# O(V^2*(V+E)) -> 시간초과

# 조금 스마트하게 생각해보자
# 한 칸을 기준으로 상하좌우로 이동할 수 있다.
# 우리는 각 점을 어떠한 그룹에 속한 한 정점이라고 생각해 볼 수 있다
# 그룹은 상하좌우로 인접한 관계에 의해 연결되어 있으며 그룹내에 한점에서 탐색을
# 진행할 경우, 이동할 수 있는 모든 정점들을 의미한다
# 벽의 상하좌우 에는, 벽 또는 그룹에 속해있는 한 정점이 존재할 것이다
# dfs를 통해 각 정점이 속해있는 그룹을 넘버링하고, 그룹의 정점의 개수를 기록해둔다
# 모든 벽의 상,하,좌,우 만을 확인하여 해당 벽과 인접한 그룹들과 그 그룹들의 정점의
# 개수의 합을 구하면, 벽에서 이동할 수 있는 칸의 개수를 구할 수 있다.
# O(V^2+(V+E)), 중복된 dfs/bfs 탐색을 하지 않으므로 시간안에 해결가능

# 체감 난이도: Gold III
# 정답률에 비해 사실 고려할 사항만 잘 고려해주면 금방 풀 수 있는 문제

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
input = stdin.readline

n, m = map(int, input().split())
_map = [[] for _ in range(n)]
for i in range(n):
    for j in map(int, input().rstrip()):
        if j == 0:
            _map[i].append(0)
        else:
            _map[i].append(-1)

cnt = {}
def dfs(r, c, num):
    _map[r][c] = num
    if num not in cnt:
        cnt[num] = 1
    else:
        cnt[num] += 1
    near_cells = [
        (r-1, c), (r, c+1), (r+1, c), (r, c-1)
    ]
    for near_cell in near_cells:
        nr, nc = near_cell
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if _map[nr][nc] != 0:
            continue
        dfs(nr, nc, num)

num = 1
for r in range(n):
    for c in range(m):
        if _map[r][c] == 0:
            dfs(r, c, num)
            num += 1

for r in range(n):
    for c in range(m):
        if _map[r][c] != -1:
            print(0, end='')
        else:
            near_cells = [
                (r-1, c), (r, c+1), (r+1, c), (r, c-1)
            ]
            groups = set()
            for near_cell in near_cells:
                nr, nc = near_cell
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                if _map[nr][nc] == -1:
                    continue
                groups.add(_map[nr][nc])
            _sum = 0
            for group in groups:
                _sum += cnt[group]
            print((_sum+1)%10, end='')
    print()