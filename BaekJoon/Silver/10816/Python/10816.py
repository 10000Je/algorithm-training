import sys

n = int(sys.stdin.readline())
memo = {}
for card in map(int, sys.stdin.readline().split()):
    if card in memo:
        memo[card] += 1
    else:
        memo[card] = 1
m = int(sys.stdin.readline())
numbers = tuple(map(int, sys.stdin.readline().split()))

for num in numbers:
    if num in memo:
        print(memo[num], end=' ')
    else:
        print(0, end=' ')
print('\n', end='')
