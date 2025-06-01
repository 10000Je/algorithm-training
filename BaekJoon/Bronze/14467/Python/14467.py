import sys

cows = [None for _ in range(11)]
cnt = 0
n = int(sys.stdin.readline())
for _ in range(n):
    cow, loc = map(int, sys.stdin.readline().split())
    if cows[cow] != None and cows[cow] != loc:
        cnt += 1
    cows[cow] = loc
print(cnt)
        