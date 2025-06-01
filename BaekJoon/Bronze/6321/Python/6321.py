import sys
n = int(sys.stdin.readline())
for i in range(0, n):
    print('String #', i+1, sep='')
    for char in sys.stdin.readline().rstrip():
        print(chr(ord(char)+1) if char != 'Z' else 'A', end='')
    print('\n')