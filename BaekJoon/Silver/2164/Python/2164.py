import sys
from collections import deque

n = int(sys.stdin.readline())
queue1 = deque()
for i in range(1, n+1):
    queue1.append(i)

last_card = queue1.popleft()
while queue1:
    queue1.append(queue1.popleft())
    last_card = queue1.popleft()
print(last_card)
