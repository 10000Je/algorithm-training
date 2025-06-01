import sys

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
arr1 = map(int, sys.stdin.readline().split())
cnt = 0
for num in arr1:
    if isPrime(num):
        cnt += 1
print(cnt)