import sys

n = int(sys.stdin.readline())
nums = [num for num in map(int, sys.stdin.readline().split())]
memo = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if nums[i] > nums[j]:
            memo[i] = max(memo[i], memo[j]+1)

print(max(memo))