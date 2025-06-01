import sys

a, b = map(int, sys.stdin.readline().split())
sum = 0
smallerNum = a if a < b else b
largerNum = b if a < b else a
print((largerNum * (largerNum+1))//2 - ((smallerNum-1)*smallerNum)//2)