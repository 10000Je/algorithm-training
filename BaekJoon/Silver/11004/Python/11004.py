import sys

n, k = map(int, sys.stdin.readline().split())
nums = [num for num in map(int, sys.stdin.readline().split())]
nums.sort()
print(nums[k-1])