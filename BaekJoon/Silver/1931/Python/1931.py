# no. 1931: 회의실 배정 (Silver I)
import sys

n = int(sys.stdin.readline())
arr1 = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr1.append((a, b))
arr1.sort(key=lambda x:(x[1], x[0]))

routes = []
cur_start = arr1[0][0]
cur_end = arr1[0][1]
routes.append(arr1[0])

for i in range(1, n):
    start, end = arr1[i][0], arr1[i][1]
    if end >= cur_end and start >= cur_end:
        cur_start = start
        cur_end = end
        routes.append((cur_start, cur_end))
print(len(routes))