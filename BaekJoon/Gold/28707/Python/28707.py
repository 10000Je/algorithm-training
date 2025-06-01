# no. 28707: 배열 정렬 (Gold I)
# 배열 A가 주어지고, 할 수 있는 조작 M개가 주어진다.
# 예를 들어, 시작 배열이 1432 이면, 목적지는 1234가 될것이다
# 이때 한 배열의 상태를 정점으로 간주할 때, 정점의 이웃은 M개의 조작만큼 존재한다
# 조작이 (1, 2), (2, 3), (3, 4), (1, 4)가 존재한다면
# 이웃은 4132, 1342, 1423, 2431이 된다
# 이러한 식으로 그래프가 구성될때, 시작점으로 부터 도착점까지의 최소거리를 구하라
# -> 다익스트라 알고리즘

# 체감 난이도: Gold II
# 배열의 상태를 노드로 간주한다는 아이디어는 매우 신박하나,
# 이것만 떠올리면 문제풀이는 일반 다익스트라와 똑같기 때문에 그리 어렵지 않은 것 같다
# 물론, 이 아이디어를 떠올리냐 못 떠올리냐가 난이도에 결정적인 영향을 끼치는건 맞는 것 같다.

from sys import stdin
import heapq
input = stdin.readline

n = int(input())
a = tuple(map(int, input().split()))
m = int(input())
b = tuple(tuple(map(int, input().split())) for _ in range(m))

def dijkstra(start, end, visited=None, unvisited=None, dist=None):
    if visited == None: visited = set()
    if unvisited == None: unvisited = [(0, start)]
    if dist == None: dist = {}
    while unvisited:
        cur_dist, cur_node = heapq.heappop(unvisited)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        dist[cur_node] = cur_dist
        for i in range(m):
            near_node = list(cur_node)
            l, r, c = b[i]
            near_node[l-1], near_node[r-1] = near_node[r-1], near_node[l-1]
            near_node = tuple(near_node)
            if near_node not in dist or dist[cur_node]+c < dist[near_node]:
                dist[near_node] = dist[cur_node]+c
                heapq.heappush(unvisited, (dist[near_node], near_node))
    if end in dist:
        return dist[end]
    else:
        return -1

end = list(a)
end.sort()
end = tuple(end)

print(dijkstra(a, end))