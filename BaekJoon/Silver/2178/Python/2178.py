import sys
from collections import deque

def bfs(maze, start, end):
    distance = {}; distance[start] = 1
    visited_vertices = set(); visited_vertices.add(start)
    queue1 = deque(); queue1.append(start)
    while queue1:
        cur_vertex = queue1.popleft()
        row, col = cur_vertex
        near_vertices = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]
        for near_vertex in near_vertices:
            near_row, near_col = near_vertex
            if near_row < 0 or near_row >= len(maze):
                continue
            if near_col < 0 or near_col >= len(maze[near_row]):
                continue
            if near_vertex in visited_vertices:
                continue
            if maze[near_row][near_col]:
                visited_vertices.add(near_vertex)
                queue1.append(near_vertex)
                distance[near_vertex] = distance[cur_vertex] + 1
    return distance[end]
        
n, m = map(int, sys.stdin.readline().split())
maze = [[int(char) for char in sys.stdin.readline().rstrip()] for i in range(n)]
print(bfs(maze, (0,0), (n-1, m-1)))
