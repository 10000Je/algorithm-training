n, k = map(int, input().split())
divisor = [i for i in range(1, n+1) if n % i == 0]
print(0 if len(divisor) < k else divisor[k-1])