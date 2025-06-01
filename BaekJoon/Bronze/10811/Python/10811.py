import sys

n, m = map(int, sys.stdin.readline().split())
memo = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    memo[i:j+1] = memo[j:i-1:-1]
print(*memo[1:])