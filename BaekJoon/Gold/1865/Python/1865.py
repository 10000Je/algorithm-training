# no. 1865: 웜홀
# 음수 사이클의 존재성을 가려내는 문제
# 음수 가중치가 존재할떄의 최단거리를 구할 수 있는
# 벨먼포드, 플로이드-와샬 알고리즘을 사용해야 한다.
# 도로는 양방향, 웜홀은 단방향인것에 주의하자.

# 추가로 벨먼포드로 풀때는 거리를 inf가 아닌 매우 큰 값으로 초기화 해야한다.
# 가령 최대로 가능한 거리는 10000 * (500) = 5_000_000 이므로 1e8 등으로 초기화
# 모든 점이 연결되어 있다는 보장이 없기 때문에 v-1 번 루프를 수행했을 때
# dist 배열에는 inf 값을 가진 값이 여전히 존재할 수 있다.
# 이때 어떠한 음수 사이클이 존재한다면 dist 배열의 값이 바뀌어야 하는게 정상이지만
# inf 값은 더하기를 하든 빼기를 하든 inf 그대로 여서 음수 사이클을 감지하질 못한다.
# 때문에 음수 사이클을 감지하기 위해선 dist 배열의 값들이 inf 값을 가져서는 안된다.

# 백준에 플로이드-와샬로 푼 버전도 제출했으니 궁금하면 확인

import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = {i: {} for i in range(1, n+1)}
    for _ in range(m):
        s, e, t = map(int, input().split())
        if e not in graph[s]:
            graph[s][e] = t
            graph[e][s] = t
        else:
            graph[s][e] = min(graph[s][e], t)
            graph[e][s] = min(graph[e][s], t)
    for _ in range(w):
        s, e, t = map(int, input().split())
        if e not in graph[s]:
            graph[s][e] = -t
        else:
            graph[s][e] = min(graph[s][e], -t)

    def belmanford(start):
        dist = {i: 1e8 for i in range(1, n+1)}
        dist[start] = 0
        for i in range(n):
            for cur_vertex in range(1, n+1):
                for near_vertex, weight in graph[cur_vertex].items():
                    if dist[cur_vertex]+weight < dist[near_vertex]:
                        dist[near_vertex] = dist[cur_vertex] + weight
                        if i == n-1:
                            return True
        return False

    has_cycle = belmanford(1)
    print("YES" if has_cycle else "NO")