import sys

n = int(sys.stdin.readline())
idx = 0
current_doomsnum = None
num = 0
while idx < n:
    if '666' in str(num):
        current_doomsnum = num
        idx += 1
    num += 1
print(current_doomsnum)
    