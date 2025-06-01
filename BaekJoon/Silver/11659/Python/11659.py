import sys

n, m = map(int, sys.stdin.readline().split())
nums = [0]
nums.extend([num for num in map(int, sys.stdin.readline().split())])

memo = [0 for i in range(n+1)]
cur_sum = 0
for i in range(n+1):
    cur_sum += nums[i]
    memo[i] = cur_sum

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(memo[end]-memo[start-1])