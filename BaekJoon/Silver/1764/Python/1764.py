import sys

n, m = map(int, sys.stdin.readline().split())
cantListen = {}
intersection = []
for i in range(n):
    name = sys.stdin.readline().rstrip()
    cantListen[name] = True
for i in range(m):
    name = sys.stdin.readline().rstrip()
    if name in cantListen:
        intersection.append(name)
intersection.sort()
print(len(intersection))
for name in intersection:
    print(name)