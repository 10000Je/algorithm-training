import sys

n = int(sys.stdin.readline())
memo = {}
for _ in range(n):
    player = sys.stdin.readline().rstrip()
    first_char = player[0]
    if first_char not in memo:
        memo[first_char] = 1
    else:
        memo[first_char] += 1
result = [key for key, value in memo.items() if value >= 5]
result.sort()
print(*result or 'PREDAJA', sep='')