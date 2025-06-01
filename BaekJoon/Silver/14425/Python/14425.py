import sys

n, m = map(int, sys.stdin.readline().split())
words = {sys.stdin.readline().rstrip() for _ in range(n)}

cnt = 0
for _ in range(m):
    cur_str = sys.stdin.readline().rstrip()
    if cur_str in words:
        cnt += 1

print(cnt)