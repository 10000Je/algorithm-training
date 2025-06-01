import sys

def getOct(num):
    nums = dict(zip('01234567', range(0,8)))
    for n in num:
        if n not in nums:
            return 0
    return int(num, base=8)

t = int(sys.stdin.readline())
for i in range(0, t):
    idx, num = sys.stdin.readline().split()
    print(idx, getOct(num), int(num), int(num, base=16), sep=' ')