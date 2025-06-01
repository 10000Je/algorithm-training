import math
import sys

nums = [[num for num in map(int, sys.stdin.readline().split())] for _ in range(9)]
max = -math.inf
loc = None
for row in range(len(nums)):
    for col in range(len(nums)):
        if nums[row][col] > max:
            max = nums[row][col]
            loc = (row+1, col+1)
print(max)
print(*loc)
