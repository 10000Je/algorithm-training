# no. 1149: RGB거리 (Silver I)
import sys

n = int(sys.stdin.readline())
memo = [[0 for _ in range(3)] for _ in range(n)]
memo[0] = [cost for cost in map(int, sys.stdin.readline().split())]

for i in range(1, n):
    # 현재가 r인경우, 이전에 g or b 을 선택한 경우의 수 중 최소값을 선택해야함
    cur_cost = [cost for cost in map(int, sys.stdin.readline().split())]
    memo[i][0] = cur_cost[0] + min(memo[i-1][1], memo[i-1][2])
    memo[i][1] = cur_cost[1] + min(memo[i-1][0], memo[i-1][2])
    memo[i][2] = cur_cost[2] + min(memo[i-1][0], memo[i-1][1])

print(min(memo[n-1]))