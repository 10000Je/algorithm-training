import sys

n = int(sys.stdin.readline())
paper = [[0 for i in range(0, 100)] for i in range(0,100)]

for i in range(0, n):
    a, b = map(int, sys.stdin.readline().split())
    for row in range(b, b+10):
        for cell in range(a, a+10):
            paper[row][cell] = 1

cnt = 0
for i in range(0, 100):
    for j in range(0, 100):
        if paper[i][j]:
            cnt += 1
print(cnt)