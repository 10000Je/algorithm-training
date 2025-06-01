import sys

str1 = sys.stdin.readline().rstrip()
memo = {}
for char in str1:
    char = char.lower()
    if char not in memo:
        memo[char] = 1
    else:
        memo[char] += 1

max = None
isMaxSeveral = False
for char in 'abcdefghijklmnopqrstuvwxyz':
    if char not in memo:
        continue
    else:
        if max == None:
            max = char
        elif memo[char] > memo[max]:
            max = char
            isMaxSeveral = False
        elif memo[char] == memo[max]:
            isMaxSeveral = True
        else:
            pass

if isMaxSeveral:
    print('?')
else:
    print(max.upper())