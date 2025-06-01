import sys

n, m = map(int, sys.stdin.readline().split())
bucket = [0 for _ in range(n+1)]
for _ in range(m):
    start, stop, num = map(int, sys.stdin.readline().split())
    for i in range(start, stop+1):
        bucket[i] = num
print(*bucket[1:])