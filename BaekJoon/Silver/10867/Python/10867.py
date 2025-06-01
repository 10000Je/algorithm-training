import sys

n = int(sys.stdin.readline())
memo = {num for num in map(int, sys.stdin.readline().split())}
nums = list(memo)
nums.sort()
print(*nums, sep=' ')