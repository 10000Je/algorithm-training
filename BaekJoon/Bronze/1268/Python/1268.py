import sys

n = int(sys.stdin.readline())
memo = [[num for num in map(int, sys.stdin.readline().split())] for _ in range(n)]
cnts = [0 for _ in range(n)]
for i in range(len(memo)):
    for j in range(len(memo)):
        for k in range(5):
            if memo[i][k] == memo[j][k]:
                cnts[i] += 1
                break
max_idx = 0
max_cnt = cnts[0]
for idx, cnt in enumerate(cnts):
    if cnt > max_cnt:
        max_idx = idx
        max_cnt = cnt
print(max_idx+1)