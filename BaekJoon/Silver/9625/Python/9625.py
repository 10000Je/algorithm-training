k = int(input())
memo = [0 for _ in range(k+1)]
memo[1] = 1
for i in range(2, k+1):
    memo[i] = memo[i-1] + memo[i-2]
print(memo[k-1], memo[k])