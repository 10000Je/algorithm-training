# no. 7579: 앱 (Gold III)
# 배낭문제와 유사한 문제이지만, 메모리의 바이트 수가 10_000_000까지 가능하기 때문에,
# 부분문제를 메모리의 바이트 수로 두고 문제를 풀려고 하면 시간초과가 될 수 있다

# 해법은, 개수(n)와 비용의 합(c)로 dp를 진행하는 것이다
# n <= 100, c1, c2, ... <= 100(c <= 10_000)을 만족하므로,
# dp 수행시 시간복잡도는 O(N*C) -> 1_000_000 으로 1초안에 해결이 된다

# dp[k][c]
# dp 테이블에는 k번째 물건을 탐색했을때, c의 비용의 합으로 확보할 수 있는
# 최대 메모리 공간 M이 저장될 것이다
# 1) 현재 앱의 실행비용이 c보다 커서 지우기가 불가능
# dp[k][c] = dp[k-1][c]
# 2) 현재 앱의 실행비용이 c보다 작아서 지우기가 가능
# dp[k][c] = max(dp[k-1][c], mem[k]+dp[k-1][c-cost[k]])

# dp 테이블을 이용해 m이상의 공간을 비울 수 있는 경우의 수중
# 가장 c가 작은 것을 찾는다

# 체감 난이도: Gold III
# 탑다운 방식으로 풀면, dp 테이블이 정상적으로 다 나오질 않아서,
# 바텀-탑 방식으로 접근했어야 했던거에 골치를 겪었다
# 그래도, dp문제 중에서는 쉬운편에 속하는 것 같다

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
mem = (0,)+tuple(map(int, input().split()))
cost = (0,)+tuple(map(int, input().split()))

sum_c = sum(cost)
dp = [[0 for _ in range(sum_c+1)] for _ in range(n+1)]

for c in range(sum_c+1):
    for k in range(1, n+1):
        if cost[k] > c:
            dp[k][c] = dp[k-1][c]
        else:
            dp[k][c] = max(dp[k-1][c], mem[k]+dp[k-1][c-cost[k]])

min_c = 1_000_000
for c in range(sum_c+1):
    for k in range(1, n+1):
        if dp[k][c] >= m:
            min_c = min(min_c, c)

print(min_c)