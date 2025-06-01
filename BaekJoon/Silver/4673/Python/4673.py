import sys

list1 = [i for i in range(1, 10001)]
for i in range(1, 10001):
    num = i
    for char in str(i):
        num += int(char)
    if num <= 10000:
        list1[num-1] = 0

for n in list1:
    if n:
        print(n)