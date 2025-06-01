import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    memo = [0 for i in range(101)]
    memo[1] = 1
    memo[2] = 1
    memo[3] = 1
    memo[4] = 2
    for j in range(5, n+1):
        memo[j] = memo[j-1] + memo[j-5]
    print(memo[n])