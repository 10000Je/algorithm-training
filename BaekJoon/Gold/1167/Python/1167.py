# no. 1167: 트리의 지름 (Gold II)
# 트리에서 임의의 두 점 사이의 거리중 가장 긴 것을 고르시오.
# 간선들의 가중치는 양수
# 두 점으로 이루어진 조합중 최단경로가 가장 긴 것이 존재하니 그 길이를 구해라!
# ...인줄 알았으나 최대거리는 루트를 거치지 않아도 잎과 잎사이의 거리도 될수있음...

# 인터넷에서 알고리즘 배움
# 한 정점을 골라 그 정점에서 제일 먼 점을 찾고
# 그 점에서 제일 먼점까지의 거리가 트리의 지름임
# 마치 원의 지름을 구하는거랑 비슷한거 같음

# 한 루트에서 자식까지의 경로는 무조건 하나다. (트리의 특징)
# 따라서 가중치가 있는 그래프에서도 dfs, bfs를 사용하여 정점-정점 사이의 거리를 구할수 있다.

import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
tree = {i: {} for i in range(1, v+1)}
for _ in range(v):
    nums = tuple(map(int, input().split()))
    start = nums[0]
    for i in range(1, len(nums)-1):
        if i % 2:
            end = nums[i]
        else:
            tree[start][end] = nums[i]
            tree[end][start] = nums[i]

def bfs(start):
    cur_queue = deque((start,))
    dist = {start: 0}
    while cur_queue:
        root = cur_queue.popleft()
        for child, weight in tree[root].items():
            if child in dist:
                continue
            cur_queue.append(child)
            dist[child] = dist[root]+weight
    return max(dist.items(), key=lambda x:x[1])

a = bfs(1)[0]
b = bfs(a)
print(b[1])