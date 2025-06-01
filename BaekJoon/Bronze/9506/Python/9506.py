import sys

n = int(sys.stdin.readline())
while n != -1:
    divisors = [i for i in range(1, n) if n % i == 0]
    if sum(divisors) != n:
        print(f'{n} is NOT perfect.')
    else:
        print(f'{n} = ', end='')
        print(*divisors, sep=' + ')
    n = int(sys.stdin.readline())