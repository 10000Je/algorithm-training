import sys

x = int(sys.stdin.readline())
n = 1
while not ((n*(n-1))//2 < x <= (n*(n+1))//2):
    n += 1
if n % 2 == 0:
    a = 1
    b = n
    for i in range((n*(n-1)//2)+1, x):
        a += 1
        b -= 1
else:
    a = 1
    b = n
    for i in range((n*(n+1)//2), x, -1):
        a += 1
        b -= 1
print(a, '/', b, sep='')