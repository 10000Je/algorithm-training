import sys
str1 = sys.stdin.readline().rstrip()
for idx, char in enumerate(str1):
    print(char, end='')
    if (idx+1) % 10 == 0:
        print('\n', end='')