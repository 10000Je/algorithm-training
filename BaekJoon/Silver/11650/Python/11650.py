import sys

n = int(sys.stdin.readline())
dots = [tuple(map(int, sys.stdin.readline().split())) for i in range(n)]
dots.sort(key=lambda x:(x[0], x[1]))
for dot in dots:
    print(dot[0], dot[1], sep=' ')