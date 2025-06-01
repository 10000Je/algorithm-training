# no. 15681: 트리와 쿼리 (Gold V)
# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력
# postorder 진행하고, 마지막에 정점의 수를 반환하도록 함수설계

# 체감 난이도: Gold V
# 트리에 대해 제대로 이해하고 있고, 후위 순회를 제대로 알고있다면
# 쉽게 dp를 설계해서 해결할 수 있는 문제이다.

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

n, r, q = map(int, input().split())
graph = {i: set() for i in range(1, n+1)}
quaries = [0 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

def traverse(root, visited=None):
    if visited == None: visited = {root}
    cnt = 1
    for child in graph[root]:
        if child in visited:
            continue
        visited.add(child)
        cnt += traverse(child, visited)
    quaries[root] = cnt
    return quaries[root]

traverse(r)

for _ in range(q):
    u = int(input())
    print(quaries[u])