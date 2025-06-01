from collections import deque
import sys

n = int(sys.stdin.readline())
queue1 = deque()
for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if 'push_front' in cmd:
        num = cmd.split().pop()
        queue1.appendleft(num)
    elif 'push_back' in cmd:
        num = cmd.split().pop()
        queue1.append(num)
    elif cmd == 'pop_front':
        if not queue1:
            print(-1)
        else:
            print(queue1.popleft())
    elif cmd == 'pop_back':
        if not queue1:
            print(-1)
        else:
            print(queue1.pop())
    elif cmd == 'size':
        print(len(queue1))
    elif cmd == 'empty':
        print(1 if not queue1 else 0)
    elif cmd == 'front':
        if not queue1:
            print(-1)
        else:
            front_value = queue1.popleft()
            queue1.appendleft(front_value)
            print(front_value)
    else:
        if not queue1:
            print(-1)
        else:
            back_value = queue1.pop()
            queue1.append(back_value)
            print(back_value)