import sys

t = int(sys.stdin.readline())
for i in range(0, t):
    n, m = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    queue = []
    for idx, priority in enumerate(priorities):
        queue.append((idx, priority))

    count = 0
    while len(queue) != 0:
        priority = queue[0][1]
        isHighestPriority = True
        for data in queue:
            other_priority = data[1]
            if other_priority > priority:
                temp = queue[0]
                del queue[0]
                queue.append(temp)
                isHighestPriority = False
                break
        if isHighestPriority:
            temp = queue[0]
            del queue[0]
            count += 1
            if temp[0] == m:
                print(count)