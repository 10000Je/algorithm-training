# no. 1005: ACM Craft (Gold III)
# 건물을 짓는 순서가 주어지고, 건물을 동시에 짓는것이 가능함
# 단, 순서를 지켜야함
# 각 건물 번호에 대해 건축이 완료되는 시간을 기록함
# 위상정렬을 수행하면, 간선을 제거하는 작업을 거치는데
# 이때, 도착하는 정점의 건축이 완료되는 시간을 갱신시켜줌
# 단, 최대값으로만 갱신시켜줘야 하며, 값이 없는 경우에는 그냥 갱신시켜준다

# 풀고나서 후기: 체감 난이도 (Gold II~III)
# 위상정렬이라는 알고리즘으로 푼다는 사실을 아는것은 1분도 안걸렸는데
# 건축이 완료되는 시간을 구하는 것이 조금 까다로운 문제였다
# 사실 반은 감으로 떄려맞치긴 했는데, 이게 정말 되나 체크하는데 시간을 조금 쓴 문제였다.
# 이후 알고리즘 분류를 보니 dp길래 왜 dp인가 했더니..
# 건축이 완료되는 시간을 구하는 알고리즘을 내가 짜고도 이게 dp인줄 몰름 ㅋㅋ
# 잘 생각해보니 dp로 푼게 맞았고, 그래서 반은 감으로 때려맞친 기분이 든거였다. (dp특임)

from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    building_times = tuple(map(int, input().split()))
    graph = {i: set() for i in range(1, n+1)}
    in_order = [0 for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].add(y)
        in_order[y] += 1
    w = int(input())
    
    def topology_sort():
        queue = deque()
        times = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if in_order[i] == 0:
                times[i] = building_times[i-1]
                queue.append(i)
        while queue:
            vertex = queue.popleft()
            for edge in graph[vertex]:
                in_order[edge] -= 1
                times[edge] = max(times[edge], times[vertex]+building_times[edge-1])
                if in_order[edge] == 0:
                    queue.append(edge)
        return times[w]
    
    time = topology_sort()
    print(time)
