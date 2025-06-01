# no. 1916: 최소비용 구하기
# 출발점-도착점 간의 최소거리, 가중치 양수 -> 다익스트라
# N <= 1000 E <= 100000
# 최적화 안된 다익스트라 사용가능...하지만 최적화로 구현

import sys
import heapq
from math import inf
input = sys.stdin.readline

n = int(input())
m = int(input())

cities = {i: {} for i in range(1, n+1)}
for _ in range(m):
    start, end, cost = map(int, input().split())
    if end not in cities[start]:
        cities[start][end] = cost
    else:
        cities[start][end] = min(cities[start][end], cost)

def dijkstra(start, end):
    unvisited_cities = [(0, start)]
    dist = {i: inf for i in range(1, n+1)}
    dist[start] = 0
    visited_cities = set()
    while unvisited_cities:
        cur_city = heapq.heappop(unvisited_cities)[1]
        if cur_city == end:
            return dist[cur_city]
        if cur_city in visited_cities:
            continue
        visited_cities.add(cur_city)
        for near_city, cost in cities[cur_city].items():
            if near_city in visited_cities:
                continue
            dist[near_city] = min(dist[near_city], dist[cur_city]+cost)
            heapq.heappush(unvisited_cities, (dist[near_city], near_city))

start, end = map(int, input().split())
min_cost = dijkstra(start, end)
print(min_cost)