# no. 12851: 숨바꼭질 2 (Gold IV)
# bfs 알고리즘 문제
# 굉장히 푸는데 어려움을 겪은 문제..
# 핵심은 이미 한 지점을 방문하는 방법이 여러가지가 있을 수 있다는 것과
# 최단거리로 방뭄하는 경로외에 다른 경로는 제외해주어야 한다는 사실이다.
# 때문에 일반 bfs와 달리 큐에 푸시하는 조건을 다르게 해주어야하며
# 조건은 현재 방문하려는(큐에 넣으려는) 정점까지의 최단거리와 현재 정점에서 방문할 정점으로 이동할 경우의 최단거리가 같은 것이다.

from collections import deque
n, k = map(int, input().split())

def bfs(start, end):
    cur_queue = deque((start,))
    dist = {start: 0}
    cnt = 0
    while cur_queue:
        cur_dot = cur_queue.popleft()
        near_dots = (
            cur_dot-1, cur_dot+1, cur_dot*2
        )
        if cur_dot == end: cnt += 1
        if end in dist and dist[cur_dot] > dist[end]:
            return dist[end], cnt
        for near_dot in near_dots:
            if near_dot < 0 or near_dot > 100_000: continue
            if near_dot not in dist:
                dist[near_dot] = dist[cur_dot] + 1
            if dist[cur_dot] + 1 == dist[near_dot]:
                cur_queue.append(near_dot)
    return dist[end], cnt

dist, cnt = bfs(n, k)
print(dist, cnt, sep='\n')