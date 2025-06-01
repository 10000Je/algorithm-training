memo = [0]
idx = n = 1
while idx <= 1000:
    for _ in range(n):
        memo.append(n)
        idx += 1
    n+=1
a, b = map(int, input().split())
print(sum(memo[a:b+1]))