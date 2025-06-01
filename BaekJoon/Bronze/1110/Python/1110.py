n = int(input())
cnt = 1
new_num = int(str(n)[-1] + str(sum([int(num) for num in str(n)]))[-1])
while n != new_num:
    cnt += 1
    new_num = int(str(new_num)[-1] + str(sum([int(num) for num in str(new_num)]))[-1])
print(cnt)