import sys

memo = {}
for i in range(0, 10):
    n = int(sys.stdin.readline())
    if n % 42 not in memo:
        memo[n%42] = True
print(len(memo))