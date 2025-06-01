import sys

n = int(sys.stdin.readline())
arr1 = []
while True:
    arr1.append(n % 9)
    if 0 < (n // 9) < 9:
        arr1.append(n // 9)
        break
    elif n // 9 == 0:
        break
    else:
        n = n // 9

for i in reversed(arr1):
    print(i, end='')
print('\n', end='')