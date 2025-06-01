import sys

t = int(sys.stdin.readline())
for i in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    if m < n:
        small = [m, x]
        big = n
        num = y
    else:
        small = [n, y]
        big = m
        num = x
    cur_small = num % small[0] if num % small[0] else small[0]
    memo = {cur_small}
    while cur_small != small[1]:      
        num += big
        cur_small = num % small[0] if num % small[0] else small[0]
        if cur_small in memo:
            print(-1)
            break
        else:
            memo.add(cur_small)
    else:
        print(num)
    