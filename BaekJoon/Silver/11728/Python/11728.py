import sys

n, m = map(int, sys.stdin.readline().split())
nums_1 = [num for num in map(int, sys.stdin.readline().split())]
nums_2 = [num for num in map(int, sys.stdin.readline().split())]
nums_1.extend(nums_2)
nums_1.sort()
print(*nums_1, sep=' ')