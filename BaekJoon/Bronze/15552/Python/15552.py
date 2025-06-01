import sys
t = int(sys.stdin.readline().rstrip())
for idx in range(0, t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)