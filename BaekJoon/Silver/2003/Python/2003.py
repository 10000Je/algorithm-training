import sys

n, m = map(int, sys.stdin.readline().split())
nums = [num for num in map(int, sys.stdin.readline().split())]

sums = [0 for _ in range(n)]
cur_sum = 0
for i in range(n):
    cur_sum += nums[i]
    sums[i] = cur_sum

cnt = 0
for i in range(n):
    for j in range(i, n):
        if sums[j] - sums[i] + nums[i] == m:
            cnt += 1

print(cnt)