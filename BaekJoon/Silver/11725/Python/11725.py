# no. 11725: 트리의 부모 찾기 (Silver II)
# 연결된 두 정점이 입력된다. 연결은 상호간으로 하고 1번노드부터 순서대로 순회하면 될거같다.
# dfs, bfs, 두가지로 풀수있는데 n이 100,000 이라 dfs 로 풀꺼면
# sys.setrecursionlimit() 으로 재귀한계를 높게 설정해주어야한다.
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = {i: set() for i in range(1, n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)

def bfs(start, current_parent=None):
    parents = {start: current_parent}
    cur_queue = deque([start])
    while cur_queue:
        cur_node = cur_queue.popleft()
        for child in tree[cur_node]:
            if child in parents:
                continue
            parents[child] = cur_node
            cur_queue.append(child)
    return parents

parents = bfs(1)
for i in range(2, n+1):
    print(parents[i])
