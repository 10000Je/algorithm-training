import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1) 

n = int(sys.stdin.readline())
str1 = str(factorial(n))
count = 0
for char in reversed(str1):
    if char == '0':
        count += 1
    else:
        break
print(count)
