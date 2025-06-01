import sys

a, b = map(int, sys.stdin.readline().split())
m, l = min(a, b), max(a, b)
n = l
while n % m:
    n += l
print(n)