import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    s, l = min(a, b), max(a, b)
    r = l % s
    while r:
        l = s
        s = r
        r = l % s
    print(a*b//s)