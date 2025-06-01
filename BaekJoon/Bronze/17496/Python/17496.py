import sys
n, t, c, p = map(int, sys.stdin.readline().split())
harvest = (n // t) if n / t > n // t else (n // t) - 1
print(c*harvest*p)