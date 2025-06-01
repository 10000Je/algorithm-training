import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [(0, 0)]
for _ in range(n):
    items.append(tuple(map(int, input().split())))
val = [[0 for _ in range(k+1)] for _ in range(n+1)]

for w in range(k+1):
    for i in range(1, n+1):
        if items[i][0] > w:
            val[i][w] = val[i-1][w]
        else:
            val[i][w] = max(val[i-1][w-items[i][0]]+items[i][1], val[i-1][w])

print(val[n][k])