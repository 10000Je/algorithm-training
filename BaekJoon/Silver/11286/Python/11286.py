import sys
import heapq

n = int(sys.stdin.readline())
heap1 = []
for i in range(n):
    x = int(sys.stdin.readline())
    if not x:
        print(heapq.heappop(heap1)[1] if heap1 else 0)
    else:
        key = abs(x)*10
        if x > 0:
            key += 1
        if x < 0:
            key -= 1
        heapq.heappush(heap1, (key, x))