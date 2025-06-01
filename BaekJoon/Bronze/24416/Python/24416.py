def fib(n, cnt=[0]):
    if n == 1 or n == 2:
        cnt[0] += 1
        return 1, cnt[0]
    else:
        return fib(n-1)[0] + fib(n-2)[0], cnt[0]

def fib2(n):
    memo = [0 for _ in range(41)]
    memo[1], memo[2] = 1, 1
    cnt = 0
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
        cnt += 1
    return memo[n], cnt

n = int(input())
print(fib(n)[1], fib2(n)[1])