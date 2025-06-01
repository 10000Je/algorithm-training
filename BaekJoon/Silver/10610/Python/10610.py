import sys

n = [num for num in sys.stdin.readline().rstrip()]
if sum(map(int, n)) % 3 == 0:
    n.sort(key=int, reverse=True)
    if n[-1] == '0':
        print(*n, sep='')
    else:
        print(-1)
else:
    print(-1)