n = int(input())
cnt = 0
for i in range(1, n+1):
    j = i
    sum = 0
    while sum < n:
        sum += j
        j += 1
    if sum == n:
        cnt += 1
print(cnt)