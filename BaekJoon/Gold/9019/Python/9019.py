import sys
from collections import deque

def bfs(start, end):
    visited_values = {start}
    route = {}
    queue1 = deque([(None, start)])
    while queue1:
        cur_vertex = queue1.popleft()
        last_path, cur_val = cur_vertex
        if cur_val == end:
            end = cur_vertex
            break
        near_vertices = [
            ('D', (cur_val*2)%10000), ('S', cur_val-1 if cur_val != 0 else 9999),
            ('L', (cur_val%1000)*10+(cur_val//1000)), ('R', (cur_val%10)*1000+(cur_val//10))
        ]
        for near_vertex in near_vertices:
            near_path, near_val = near_vertex
            if near_val in visited_values:
                continue
            queue1.append(near_vertex)
            visited_values.add(near_val)
            route[near_val] = (near_path, cur_val)
    shortest_path = deque()
    current_vertex = end
    while current_vertex[1] != start:
        shortest_path.appendleft(route[current_vertex[1]][0])
        current_vertex = route[current_vertex[1]]
    return shortest_path

t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(''.join(bfs(a, b)))
    
