n, k = map(int, input().split())
nums = [i for i in range(n+1)]
nums[0] = nums[1] = 0
cnt = 0
for i in range(2, n+1):
    if not nums[i]:
        continue
    for j in range(i, n+1, i):
        if not nums[j]:
            continue
        nums[j] = 0
        cnt += 1
        if cnt == k:
            print(j)
            break
    else:
        continue
    break