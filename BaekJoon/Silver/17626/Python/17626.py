import math

n = int(input())
memo = [0 for i in range(n+1)]
memo[1] = 1
for i in range(2, n+1):
    if int(i**0.5) == i**0.5:
        memo[i] = 1
    else:
        memo[i] = math.inf
        for j in range(1, int(i**0.5)+1):
            memo[i] = min(memo[i], memo[j**2]+memo[i-j**2])
print(memo[n])
