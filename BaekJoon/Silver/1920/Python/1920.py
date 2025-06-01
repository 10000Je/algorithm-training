import sys

n = int(sys.stdin.readline())
memo = {}

for num in map(int, sys.stdin.readline().split()):
    memo[num] = True

m = int(sys.stdin.readline())
for num in map(int, sys.stdin.readline().split()):
    if num in memo:
        print('1')
    else:
        print('0')