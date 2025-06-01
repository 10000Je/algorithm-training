import sys

m = int(sys.stdin.readline())
set1 = set()

for i in range(m):
    cmd = sys.stdin.readline().rstrip()
    if 'add' in cmd:
        n = int(cmd.split().pop())
        if n not in set1:
            set1.add(n)
    elif 'remove' in cmd:
        n = int(cmd.split().pop())
        if n in set1:
            set1.remove(n)
    elif 'check' in cmd:
        n = int(cmd.split().pop())
        print(1 if n in set1 else 0)
    elif 'toggle' in cmd:
        n = int(cmd.split().pop())
        if n in set1:
            set1.remove(n)
        else:
            set1.add(n)
    elif cmd == 'all':
        set1 = set(range(1, 21))
    else:
        set1.clear()