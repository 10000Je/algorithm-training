import sys

t = int(sys.stdin.readline())
for _ in range(t):
    nums = [num for num in map(int, sys.stdin.readline().split())]
    nums.sort()
    print(nums[-3])