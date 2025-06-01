import math, sys

cur_p = 0
min_d = math.inf
max_p = -math.inf
for i in range(10):
    point = int(sys.stdin.readline())
    cur_p += point
    cur_d = abs(100-cur_p)
    if cur_d < min_d:
        min_d = cur_d
        max_p = cur_p
    elif cur_d == min_d and cur_p > max_p:
        max_p = cur_p
print(max_p)