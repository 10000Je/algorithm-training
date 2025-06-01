import sys

def dfs_traverse(graph, start_vertex, visited_vertices=set()):
    visited_vertices.add(start_vertex)
    if start_vertex not in graph:
        return visited_vertices
    for adjacent_vertex in graph[start_vertex]:
        if adjacent_vertex in visited_vertices:
            continue
        dfs_traverse(graph, adjacent_vertex, visited_vertices)
    return visited_vertices

n = int(sys.stdin.readline())
num_of_edge = int(sys.stdin.readline())
graph = {}

for i in range(num_of_edge):
    vertex, adjacent_vertex = map(int, sys.stdin.readline().split())
    if vertex not in graph:
        graph[vertex] = [adjacent_vertex]
    else:
        graph[vertex].append(adjacent_vertex)
    if adjacent_vertex not in graph:
        graph[adjacent_vertex] = [vertex]
    else:
        graph[adjacent_vertex].append(vertex)
        
print(len(dfs_traverse(graph, 1))-1)