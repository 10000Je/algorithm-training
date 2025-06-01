# no. 16953: A->B (Silver II)
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 2를 곱하기, 1을 수의 가장 오른쪽에 추가하기다
# 필요한 연산의 최솟값을 구해보자.
# bfs 알고리즘 문제(A와 B사이의 연산의 최소거리를 구하라)

from collections import deque

a, b = map(int, input().split())
limit = 10**9

def bfs(start, end):
    cur_queue = deque((start, ))
    dist = {start: 0}
    while cur_queue:
        cur_num = cur_queue.popleft()
        if cur_num == end:
            return dist[cur_num]+1
        near_nums = [cur_num*2, cur_num*10+1]
        for near_num in near_nums:
            if near_num > limit:
                continue
            if near_num in dist:
                continue
            dist[near_num] = dist[cur_num] + 1
            cur_queue.append(near_num)
    return -1

print(bfs(a, b))