import sys
import math

n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(n)]
ropes.sort(reverse=True)

max_weight = -math.inf
for i in range(n):
    min_rope = ropes[i]
    cur_weight = min_rope * (i+1)
    max_weight = max(max_weight, cur_weight)

print(max_weight)