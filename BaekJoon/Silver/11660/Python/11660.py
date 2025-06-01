# no. 11660: 구간 합 구하기 5 (Silver I)
# 표의 크기 N <= 1024
# 합을 구해야하는 횟수 M <= 100000
# 매번 표를 순회하며 합을 계산하면 무조건 시간초과
# 미리 계산한 값을 재활용해야한다...

# n*n 크기의 새로운 배열을 만든다.
# 각 셀에는 0,0 칸부터 r, c 칸 까지의 합을 넣는다.
# 이후 (r1, c1) - (r2, c2) 거리를 구할때는
# memo[r2][c2] - memo[r2][c1-1] - memo[r1-1][c2] + memo[r1-1][c1-1] 가 답이된다.

# sums 2차원 배열에 숫자를 채워넣을때
# sums[r][c] = nums[r][c] + sums[r-1][c] + sums[r][c-1] - sums[r-1][c-1] 이다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j, num in enumerate(map(int, input().split())):
        nums[i][j+1] = num

sums = [[0 for _ in range(n+1)] for _ in range(n+1)]
for r in range(1, n+1):
    for c in range(1, n+1):
        sums[r][c] = nums[r][c] + sums[r-1][c] + sums[r][c-1] - sums[r-1][c-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sums[x2][y2]-sums[x2][y1-1]-sums[x1-1][y2]+sums[x1-1][y1-1])