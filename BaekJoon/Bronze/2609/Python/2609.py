import sys

a, b = map(int, sys.stdin.readline().split())
if a < b:
    a, b = b, a

largerNum, smallerNum = a, b
r = None
while r != 0:
    r = a % b
    a = b
    b = r
    
print(a)
print((smallerNum // a)*largerNum)