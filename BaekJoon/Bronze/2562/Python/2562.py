import sys
index = 0
max = 0
for idx in range(0, 9):
    num = int(sys.stdin.readline().strip())
    if num > max:
        max = num
        index = idx+1
print(max, index, sep='\n')