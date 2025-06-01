# no 2342: Dance Dance Revolution (Gold III)
# n번째 지시사항까지 완료하는데 드는 최소 힘을 구해라
# 매순간 최소의 힘만 들여서 전체의 최적해를 만들 수 있는가?
# -> 현재 선택이 이후의 선택에 영향을 줄 수 있기 때문에 불가능 (그리디 불가능)
# dp 접근
# n번째 지시사항까지 완료하는데 드는 최소 힘
# 상태정의 -> 현재 왼발/오른발 위치, 완료한 지시사항
# dp[n][0-4][0-4] 로 dp 테이블 정의 (inf로 초기화)
# dp[n][i][j]
# dp[n-1][0-4][0-4] 부터 i,j 로 발을 바꾸는데 필요한 최소 비용을 저장
# 단, 발의 위치 i, j 가 지시사항과 위배되거나 두 발이 똑같은 위치에 있는 경우는
# 계산하지 않고 inf로 남겨둠

# 체감 난이도: Gold III
# 구현이 조금 힘든 dp문제긴 하지만, cost구현만 잘 해주면 쉬운문제
# 듣자하니 top-down 방식보다 bottom-up 방식이 더 편하다고 한다

from sys import stdin
from math import inf
input = stdin.readline

locs = [0] + list(map(int, input().split()))
locs.pop()
n = len(locs)-1
dp = [[[inf for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
dp[0][0][0] = 0

for i in range(1, n+1):
    for j in range(5):
        for k in range(5):
            if j == k or (j != locs[i] and k != locs[i]):
                continue
            for left in range(5):
                for right in range(5):
                    cost = 0
                    if left == j:
                        if left == locs[i]:
                            cost += 1
                    else:
                        if left == 0:
                            cost += 2
                        else:
                            if abs(j-left) == 2:
                                cost += 4
                            else:
                                cost += 3
                    if right == k:
                        if right == locs[i]:
                            cost += 1
                    else:
                        if right == 0:
                            cost += 2
                        else:
                            if abs(k-right) == 2:
                                cost += 4
                            else:
                                cost += 3
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][left][right]+cost)

_min = inf
for arr in dp[n]:
    for cost in arr:
        _min = min(_min, cost)

print(_min)