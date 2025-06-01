import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    p = [char for char in sys.stdin.readline().rstrip()]
    n = int(sys.stdin.readline())
    if n <= 0:
        sys.stdin.readline().rstrip()
        nums = deque()
    else:
        nums = deque(sys.stdin.readline().rstrip().strip('[]').split(','))
    is_reversed = False
    for fn in p:
        if fn == 'R':
            is_reversed = True if not is_reversed else False
        if fn == 'D':
            if not nums:
                print('error')
                is_errored = True
                break
            else:
                if is_reversed:
                    nums.pop()
                else:
                    nums.popleft()
    else:
        print('[', end='')
        if is_reversed:
            print(','.join(reversed(nums)), end=']\n')
        else:
            print(','.join(nums), end=']\n')