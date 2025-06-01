# no. 1799: 비숍 (Gold I)
# ver1: 백트래킹
# 처음에는 그냥 일반적인 백트래킹 해법으로 접근하여 O((n^2)!)해법으로 접근했다가
# 비참하게 시간초과를 맞고말았다. (심지어 채점서버 버그나서 기다리는 중에서 1시간을..)
# 이후 평범하게 접근할 순 없음을 깨닫고 나름의 접근법을 떠올리고자 했다

# 이 문제는 가지치기가 핵심인 문제이다.
# 체스판 위의 한 칸의 상태는 2가지, 비숍이 있음과 없음으로 나눌 수 있다.
# 단순하게 접근하면 모든 칸에 대해 2가지 경우의 수가 있으므로 그대로 백트래킹을 진행하면
# 2^100의 시간복잡도로 인해 개같이 망하고 만다

# 여기서 체스를 해봤으면 한번쯤 들어봤을 개념을 적용할 수 있다.
# 밝은색 비숍과 어두운색 비숍은 서로에게 아무런 영향을 끼치지 못한다.
# 대각선만 이동가능하다는건, 같은 색의 대각선으로만 이동이 가능하다는 것을 의미한다
# 따라서, 밝은색 비숍의 배치는 어두운색 비숍의 배치에 아무런 영향을 끼치지 못하고
# 반대의 경우에도 마찬가지이다.
# 따라서, 체스판을 절반으로 나누어, 밝은색 비숍의 최대개수와 어두운색 비숍의 최대개수를 합하면
# 전체의 합을 구할 수 있다. (중간에서 만나기 알고리즘) -> 2^50 + 2^50 -> 가지치기 적절히 할경우 가능

# 체감 난이도 : Gold I
# 골드1 다운 난이도였다...중간에서 만나기와 대각선 판별이 힘들었던 문제

from sys import stdin
input = stdin.readline

n = int(input())
board = tuple(tuple(map(int, input().split())) for _ in range(n))

dark_bishops = []
light_bishops = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 0: continue
        if (r+c) % 2 == 0:
            dark_bishops.append((r, c))
        else:
            light_bishops.append((r, c))

dark_diag = {}
light_diag = {}
for r, c in dark_bishops:
    dark_diag[(r, c)] = [(r+c)//2, (r-c+n-1)//2+n]

for r, c in light_bishops:
    light_diag[(r, c)] = [(r+c)//2, (r-c+n-1)//2+n]

def dark_backtrack(using_diag=0, cur_idx=-1):
    if not dark_bishops: return 0
    if cur_idx == -1:
        new_diag = using_diag
        for diag in dark_diag[dark_bishops[cur_idx+1]]:
            new_diag = new_diag | (1 << diag)
        p1 = dark_backtrack(new_diag, 0) + 1
        p2 = dark_backtrack(using_diag, 0)
        return max(p1, p2)
    elif 0 <= cur_idx < len(dark_bishops)-1:
        new_diag = using_diag
        for diag in dark_diag[dark_bishops[cur_idx+1]]:
            if (1 << diag) & using_diag:
                return dark_backtrack(using_diag, cur_idx+1)
            else:
                new_diag = new_diag | (1 << diag)
        p1 = dark_backtrack(new_diag, cur_idx+1) + 1
        p2 = dark_backtrack(using_diag, cur_idx+1)
        return max(p1, p2)
    else:
        return 0

def light_backtrack(using_diag=0, cur_idx=-1):
    if not light_bishops: return 0
    if cur_idx == -1:
        new_diag = using_diag
        for diag in light_diag[light_bishops[cur_idx+1]]:
            new_diag = new_diag | (1 << diag)
        p1 = light_backtrack(new_diag, 0) + 1
        p2 = light_backtrack(using_diag, 0)
        return max(p1, p2)
    elif 0 <= cur_idx < len(light_bishops)-1:
        new_diag = using_diag
        for diag in light_diag[light_bishops[cur_idx+1]]:
            if (1 << diag) & using_diag:
                return light_backtrack(using_diag, cur_idx+1)
            else:
                new_diag = new_diag | (1 << diag)
        p1 = light_backtrack(new_diag, cur_idx+1) + 1
        p2 = light_backtrack(using_diag, cur_idx+1)
        return max(p1, p2)
    else:
        return 0

print(dark_backtrack()+light_backtrack())
