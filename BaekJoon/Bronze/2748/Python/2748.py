n = int(input())
memo = [0 for _ in range(91)]
memo[0], memo[1] = 0, 1
for i in range(2, n+1):
    memo[i] = memo[i-1] + memo[i-2]
print(memo[n])