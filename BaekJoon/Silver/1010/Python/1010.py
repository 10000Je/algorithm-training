import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    smallerNum = n if n < m else m
    largerNum = m if n < m else n
    print(factorial(largerNum)//(factorial(smallerNum)*factorial(largerNum-smallerNum)))