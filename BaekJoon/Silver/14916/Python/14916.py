n = int(input())
cnt = n // 5
while (n-(cnt*5)) % 2:
    cnt -= 1
    if cnt < 0:
        print(cnt)
        break
else:
    cnt += (n-cnt*5) // 2
    print(cnt)