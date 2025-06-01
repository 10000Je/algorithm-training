import sys
n = int(sys.stdin.readline().strip())
number_list = list(map(int, sys.stdin.readline().split()))
min = max = number_list[0]
for num in number_list:
    if num < min:
        min = num
    if num > max:
        max = num
print(min, max)