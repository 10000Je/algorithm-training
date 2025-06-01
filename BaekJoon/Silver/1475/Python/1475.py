import sys
from math import ceil

n = int(sys.stdin.readline())
memo = {}
for char in str(n):
    num = int(char)
    if num == 6 or num == 9:
        num = 6
    if num in memo:
        memo[num] += 1
    else:
        memo[num] = 1
if 6 in memo:
    memo[6] = ceil(memo[6] / 2)
print(max(memo.values()))