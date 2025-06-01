from collections import deque
import sys

n = int(sys.stdin.readline())
queue1 = deque()
for i in range(0, n):
    cmd = sys.stdin.readline().rstrip()
    if 'push' in cmd:
        num = cmd.split().pop()
        queue1.append(num)
    elif cmd == 'front':
        if not queue1:
            print(-1)
        else:
            front_value = queue1.popleft()
            queue1.appendleft(front_value)
            print(front_value)
    elif cmd == 'back':
        if not queue1:
            print(-1)
        else:
            back_value = queue1.pop()
            queue1.append(back_value)
            print(back_value)
    elif cmd == 'pop':
        if not queue1:
            print(-1)
        else:
            print(queue1.popleft())
    elif cmd == 'size':
        print(len(queue1))
    else:
        print(1 if not queue1 else 0)
