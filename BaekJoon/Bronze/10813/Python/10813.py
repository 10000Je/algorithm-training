import sys

n, m = map(int, sys.stdin.readline().split())
bucket = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]
print(*bucket[1:])    
