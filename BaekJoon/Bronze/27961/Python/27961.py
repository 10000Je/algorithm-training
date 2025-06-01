# no. 27961: 고양이는 많은수록 좋다

n = int(input())
cnt = 0
if n == 0:
    print(0)
else:
    while n > 1:
        if n % 2:
            n = (n//2)+1
        else:
            n = (n//2)
        cnt += 1
    print(cnt+1)