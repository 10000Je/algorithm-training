nums = [num for num in map(int, input().split())]
nums.sort()
limit = nums[-1]*nums[-2]*nums[-3]
for i in range(1, limit+1):
    cnt = 0
    for num in nums:
        if i % num == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break