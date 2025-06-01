import sys

x = int(sys.stdin.readline())
memo = [0 for i in range(x+1)]
for i in range(2, x+1):
    if i % 3 == 0 and i % 2 == 0:
        memo[i] = min(memo[i//3]+1, memo[i//2]+1, memo[i-1]+1)
    elif i % 3 == 0:
        memo[i] = min(memo[i//3]+1, memo[i-1]+1)
    elif i % 2 == 0:
        memo[i] = min(memo[i//2]+1, memo[i-1]+1)
    else:
        memo[i] = memo[i-1]+1
print(memo[x])