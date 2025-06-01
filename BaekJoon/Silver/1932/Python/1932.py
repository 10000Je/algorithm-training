import sys

n = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

memo = [[0 for _ in range(i)] for i in range(1, n+1)]
memo[0][0] = nums[0][0]
for floor in range(1, n):
    for cell in range(len(nums[floor])):
        if cell == 0:
            memo[floor][cell] = memo[floor-1][cell] + nums[floor][cell]
        elif cell == len(nums[floor])-1:
            memo[floor][cell] = memo[floor-1][cell-1] + nums[floor][cell]
        else:
            memo[floor][cell] = max(memo[floor-1][cell-1]+nums[floor][cell], memo[floor-1][cell]+nums[floor][cell])

print(max(memo[n-1]))