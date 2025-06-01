import sys

n = int(sys.stdin.readline())
for i in range(0, n):
    str1 = sys.stdin.readline().rstrip()
    point = 1
    sum = 0
    for char in str1:
        if char == 'O':
            sum += point
            point += 1
        else:
            point = 1
    print(sum)