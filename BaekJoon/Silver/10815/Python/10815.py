import sys

n = int(sys.stdin.readline())
cards = {}
for card in map(int, sys.stdin.readline().split()):
    cards[card] = True
m = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().split())

for num in nums:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
print('\n', end='')