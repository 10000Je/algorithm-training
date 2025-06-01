import sys
import heapq

n = int(sys.stdin.readline())
heap1 = []
for i in range(n):
    cmd = int(sys.stdin.readline())
    if not cmd:
        print((-1)*heapq.heappop(heap1) if heap1 else 0)
    else:
        heapq.heappush(heap1, (-1)*cmd)