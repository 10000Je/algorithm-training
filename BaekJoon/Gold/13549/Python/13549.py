# no. 13549: 숨바꼭질 3 (Gold V)
# 수빈이는 걸을때는 1초 후에 X-1 또는 X+1 로 이동
# 텔포할때는 0초만에 즉 바로 2*X로 이동
# bfs 알고리즘, 하지만 텔포에 유의하여 작성
# 0-1 bfs 알고리즘 참고 (근데 스스로 생각해서 품)
from collections import deque

n, k = map(int, input().split())

def bfs(start, end):
    dist = {start: 0}
    cur_queue = deque((start,))
    while cur_queue:
        cur_dot = cur_queue.popleft()
        if cur_dot == end:
            return dist[end]
        tp_dot = cur_dot * 2
        if 0 <= tp_dot <= 100_000 and tp_dot not in dist:
            dist[tp_dot] = dist[cur_dot]
            cur_queue.appendleft(tp_dot)
        near_dots = (cur_dot-1, cur_dot+1)
        for near_dot in near_dots:
            if 0 <= near_dot <= 100_000 and near_dot not in dist:
                dist[near_dot] = dist[cur_dot]+1
                cur_queue.append(near_dot)

print(bfs(n, k))
