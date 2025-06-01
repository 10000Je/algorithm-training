import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    r = a % 10
    for _ in range(b-1):
        r = (r*a) % 10
    print(r if r else 10)