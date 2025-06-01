import sys

n, m = map(int, sys.stdin.readline().split())
trees = [tree for tree in map(int, sys.stdin.readline().split())]
lowest = 0
highest = 1_000_000_000
max_height = 0
while lowest <= highest:
    mid = (highest+lowest)//2
    cnt = 0
    for height in trees:
        if height > mid:
            cnt += (height-mid)
    if cnt < m:
        highest = mid-1
    elif cnt >= m:
        max_height = mid
        lowest = mid+1
print(max_height)