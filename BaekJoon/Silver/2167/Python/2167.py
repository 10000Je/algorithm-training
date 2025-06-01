import sys

n, m = map(int, sys.stdin.readline().split())
nums = [[num for num in map(int, sys.stdin.readline().split())] for _ in range(n)]
k = int(sys.stdin.readline())
for _ in range(k):
    start_row, start_col, end_row, end_col = map(int, sys.stdin.readline().split())
    cur_sum = 0
    for row in range(start_row-1, end_row):
        for col in range(start_col-1, end_col):
            cur_sum += nums[row][col]
    print(cur_sum)