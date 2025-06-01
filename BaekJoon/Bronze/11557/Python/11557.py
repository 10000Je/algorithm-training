import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    memo = {}
    for _ in range(n):
        s, l = sys.stdin.readline().split()
        l = int(l)
        if s not in memo:
            memo[s] = l
        else:
            memo[s] += l
    print(max(memo.items(), key=lambda x:x[1])[0])