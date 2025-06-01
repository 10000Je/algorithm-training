# no. 1766: 문제집 (Gold II)
# 위상정렬에서는 진입차수가 0인 정점들을 큐에 넣고 관리한다
# 하지만 이 문제에서는 "난이도가 쉬운" 즉, 번호가 낮은 문제부터
# 먼저 풀어야 하므로, 진입차수가 0인 정점들 중 번호가 가장 낮은
# 정점부터 먼저 팝해줘야한다. 이는 우선순위 큐를 통해 구현가능하다.
# heap 자료구조를 이용하며 O(logN)안에 팝이 가능하며 이때의 시간복잡도는
# O(VlogV+E)가 되므로, 시간복잡도 조건도 충족한다.

# 후기: 
# 체감 난이도: Gold III
# 사실 푸는건 별로 안걸렸는데 문제가 조금 애매하게 설명해주는 부분이 없지않아서
# 여기서 만약 헤맸으면 시간 좀 썼을 것 같은 문제다
# 핵심은, 집입차수가 0인 정점들 중에서, 번호가 가장 낮은것을 먼저 뽑아야 한다는 것이다
# 이는 단순히 큐로 관리하던 정점들을 우선순위 큐로 바꿔주면 해결되는 부분이라
# 문제해결이 쉬웠던 것 같다.

import heapq
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = {i: set() for i in range(1, n+1)}
inorders = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    inorders[b] += 1

pri_queue = []
for i in range(1, n+1):
    if inorders[i] == 0:
        heapq.heappush(pri_queue, i)

# topology_sort
result = []
while pri_queue:
    cur_vertex = heapq.heappop(pri_queue)
    result.append(cur_vertex)
    for edge in graph[cur_vertex]:
        inorders[edge] -= 1
        if inorders[edge] == 0:
            heapq.heappush(pri_queue, edge)

print(*result)