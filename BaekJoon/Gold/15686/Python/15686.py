# no. 15686: 치킨 배달 (Gold V, Class 4)

# 간선간의 가중치는 전부다 1로 동일하다. (bfs 사용가능)
# 근데 bfs를 이용해야할까?
# 2차원 배열을 받고, 그 중에서 집과 치킨집의 위치 만을 받아도 된다.
# 왜냐하면 그 사이를 가로막는 장애물(벽)이 없기 때문이다.
# 이 경우 최단 거리는 abs(r1-r2) + abs(c1-c2) 로 정의된다.
# 집에서 가장 가까운 치킨집의 거리 -> 치킨 거리
# 도시의 치킨거리 -> 모든 집의 치킨거리의 합

# 도시의 치킨집 중에서 최대 M개를 고르는데, 이때 도시의 치킨거리가 최소가 되게끔
# 골라야한다.

# M개를 고른 조합중에 도시의 치킨거리의 최소값을 찾아야한다.
# 백트래킹으로 풀수 있을거같은데...
# 13 C m 의 복잡도 -> 13 C 6 이 최대가 될것이고... -> 아마도 가능
# 13-m 개의 치킨집을 제외하고, 그떄의 각 도시의 최대거리 중 최소값을 찾으면 될듯
# 가지치기... -> 치킨집을 제외하는 순서는 고려대상이 아니다.
# 즉 항상 오름차순으로 치킨집을 제외하도록 하면 똑같은 치킨집을 다른 순서로 제외하는 경우
# 들은 연산대상에서 제외할 수 있다.
# 치킨집을 제외할 때마다 인덱스를 기록해서 해당 인덱스들 중 최대값보다 큰 인덱스의 치킨집만
# 제외하면 치킨집을 항상 오름차순으로 제외할 수 있다.

import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
cur_map = [list(map(int, input().split())) for _ in range(n)]
homes = [(row, col) for row in range(n) for col in range(n) if cur_map[row][col] == 1]
chickens = [(row, col) for row in range(n) for col in range(n) if cur_map[row][col] == 2]

def backtracking(excluded_chickens=set(), min_dist=[math.inf]):
    if len(chickens)-len(excluded_chickens) == m:
        sum_dist = 0
        for home in homes:
            cur_dist = math.inf
            for idx, chicken in enumerate(chickens):
                if idx in excluded_chickens:
                    continue
                cur_dist = min(cur_dist, abs(chicken[0]-home[0])+abs(chicken[1]-home[1]))
            sum_dist += cur_dist
        min_dist[0] = min(min_dist[0], sum_dist)
        return min_dist[0]
    for idx in range(len(chickens)):
        if excluded_chickens and idx <= max(excluded_chickens):
            continue
        new_excluded_chickens = excluded_chickens.copy()
        new_excluded_chickens.add(idx)
        backtracking(new_excluded_chickens, min_dist)
    return min_dist[0]

min_dist = backtracking()
print(min_dist)