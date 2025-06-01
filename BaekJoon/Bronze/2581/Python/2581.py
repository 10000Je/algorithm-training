import sys

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
prime_numbers = []

for i in range(m, n+1):
    if isPrime(i):
        prime_numbers.append(i)

if len(prime_numbers) == 0:
    print(-1)
else:
    sum = 0
    min = prime_numbers[0]
    for prime_number in prime_numbers:
        sum += prime_number
        if prime_number < min:
            min = prime_number
    print(sum)
    print(min)