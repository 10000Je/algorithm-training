# no. 2252: 줄 세우기 (Gold III)
# 이게...왜...위상정렬...?
# 위상정렬... 방향 비순환 그래프에서 올바른 순서로 정렬하는 알고리즘...
# a가 b앞에 서야한다는건 a정점에서 b정점 방향의 간선이 있다는 것을 의미함
# 이는 일종의 방향 그래프가 되고, 키의 순서에는 사이클이 존재하지 않으므로
# 방향 비순환 그래프라는 조건을 충족함

# 위상정렬에서 필요한 것
# 정점의 정보(진입차수, 간선들의 도착점)

from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
in_degree = [0 for _ in range(n+1)]
edges = {i: set() for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].add(b) # a에서 나가는 간선을 추가
    in_degree[b] += 1 # b의 진입차수를 증가

def topology_sort():
    queue = deque(tuple(i for i in range(1, n+1) if in_degree[i]==0))
    result = []
    while queue:
        cur_vertex = queue.popleft()
        result.append(cur_vertex)
        for dest in edges[cur_vertex]:
            in_degree[dest] -= 1 # 간선을 제거
            if in_degree[dest] == 0: # 만약 진입차수가 0이 되었다면
                queue.append(dest) # 큐에 추가
    return result

result = topology_sort()
print(*result)