import sys

n = int(sys.stdin.readline())
dots = 5
for i in range(2, n+1):
    dots = dots + i*5 - (2*i-1)
print(dots % 45678)