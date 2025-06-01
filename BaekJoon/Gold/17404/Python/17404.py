# no. 17404: RGB 거리 2 (Gold IV)
# 동적 프로그래밍 (dp) 문제
# 일단, i번째 집과 i-1번째 집의 색이 다르다는 조건을 지키면서
# 집의 색을 칠한다면 i번째집은 i-1번째 집과 i+1번째 집과 색이 다를수 밖에 없다.
# 다만 이 문제에서는 특수한 경우가 있는데
# 바로 첫번째 집과, 마지막 집의 경우이다
# 첫번째 집은 n번째 집과 2번째 집과 색이 같아선 안되며
# n번재 집은 n-1번째 집과 첫번째 집과 색이 같아선 안된다

# 이 때문에 단순한 dp로 해법을 할 경우, 첫번째 집과 마지막 집의 색이 같은경우도
# 포함해버릴 수 있기 때문에, 첫번째 집을 각각 r, g, b로 정한 경우의 수중
# 최소값을 갖는 것을 출력해줘야한다

# 체감 난이도: Gold V
# 처음을 고정하면 문제가 쉽게 풀린다는걸 캐치한다면 어렵지 않다
# 다만 이를 캐치하지 못한다면 조금 헤맬수도 있는 문제

from sys import stdin
from math import inf
input = stdin.readline

n = int(input())
cost = tuple(tuple(map(int, input().split())) for _ in range(n))

rdp = [[inf, inf, inf] for _ in range(n)]
rdp[0][0] = cost[0][0]

for i in range(1, n-1):
    rdp[i][0] = min(rdp[i-1][1], rdp[i-1][2]) + cost[i][0]
    rdp[i][1] = min(rdp[i-1][0], rdp[i-1][2]) + cost[i][1]
    rdp[i][2] = min(rdp[i-1][0], rdp[i-1][1]) + cost[i][2]

rdp[n-1][0] = inf
rdp[n-1][1] = min(rdp[n-2][0], rdp[n-2][2]) + cost[n-1][1]
rdp[n-1][2] = min(rdp[n-2][0], rdp[n-2][1]) + cost[n-1][2]

gdp = [[inf, inf, inf] for _ in range(n)]
gdp[0][1] = cost[0][1]

for i in range(1, n-1):
    gdp[i][0] = min(gdp[i-1][1], gdp[i-1][2]) + cost[i][0]
    gdp[i][1] = min(gdp[i-1][0], gdp[i-1][2]) + cost[i][1]
    gdp[i][2] = min(gdp[i-1][0], gdp[i-1][1]) + cost[i][2]

gdp[n-1][0] = min(gdp[n-2][1], gdp[n-2][2]) + cost[n-1][0]
gdp[n-1][1] = inf
gdp[n-1][2] = min(gdp[n-2][0], gdp[n-2][1]) + cost[n-1][2]

bdp = [[inf, inf, inf] for _ in range(n)]
bdp[0][2] = cost[0][2]

for i in range(1, n-1):
    bdp[i][0] = min(bdp[i-1][1], bdp[i-1][2]) + cost[i][0]
    bdp[i][1] = min(bdp[i-1][0], bdp[i-1][2]) + cost[i][1]
    bdp[i][2] = min(bdp[i-1][0], bdp[i-1][1]) + cost[i][2]

bdp[n-1][0] = min(bdp[n-2][1], bdp[n-2][2]) + cost[n-1][0]
bdp[n-1][1] = min(bdp[n-2][0], bdp[n-2][2]) + cost[n-1][1]
bdp[n-1][2] = inf

print(min(min(rdp[n-1]), min(gdp[n-1]), min(bdp[n-1])))