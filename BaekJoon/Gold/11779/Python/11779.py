# no. 11779: 최소비용 구하기 2 (Gold III)
# 버스비용은 양의 정수 -> 양의 가중치 그래프
# 도시 1000개, 버스 100000개 -> 다익스트라
# 경로 출력 해주어야함

from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
m = int(input())

cities = {i: {} for i in range(1, n+1)}
for _ in range(m):
    start, end, cost = map(int, input().split())
    if end not in cities[start]:
        cities[start][end] = cost
    else:
        cities[start][end] = min(cities[start][end], cost)

start, end = map(int, input().split())

def dijkstra(start, end):
    unvisited_cities = [(0, start)]
    visited_cities = set()
    dist = {i: 10**9 for i in range(1, n+1)}
    dist[start] = 0
    route = {start: -1}
    while unvisited_cities:
        cur_city = heappop(unvisited_cities)[1]
        if cur_city == end:
            break
        if cur_city in visited_cities: continue
        visited_cities.add(cur_city)
        for near_city, cost in cities[cur_city].items():
            if near_city in visited_cities: continue
            if dist[cur_city]+cost < dist[near_city]:
                dist[near_city] = dist[cur_city]+cost
                route[near_city] = cur_city
                heappush(unvisited_cities, (dist[near_city], near_city))
    path = []
    cur_city = end
    while cur_city != -1:
        path.append(cur_city)
        cur_city = route[cur_city]
    path.reverse()
    return dist[end], path

dist, path = dijkstra(start, end)
print(dist)
print(len(path))
print(*path)