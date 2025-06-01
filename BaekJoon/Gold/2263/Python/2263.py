# no. 2263: 트리의 순회 (Gold I)
# 한동안 헤매다가 결국, post_order를 이용하면 분할정복을 통해
# 부모노드로 부터 자식노드를 구할 수 있음을 파악하고
# 분할정복으로 접근시도

# nameerror -> 오타였음
# recursion error -> 노드가 10만개 이하이기 떄문에, 일반적인 재귀깊이로는 오류발생
# setrecursionlimit을 통해 재귀제한을 늘려줌
# pypy3 제출시 메모리 초과, python3 제출했더니 성공

# 체감 난이도: Gold I
# 분할정복의 구현이 다른 것들에 비해 어렵고, 접근도 상당히 빡쎗지만
# 그래도, 끝까지 노력하면 풀 수 있는 문제. 자신의 해답을 믿어야했던
# 신뢰의 도약같은 문제였다.

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
in_order = list(map(int, input().split()))
in_idx = [0 for _ in range(n+1)]

for i in range(n):
	in_idx[in_order[i]] = i
post_order = list(map(int, input().split()))

def make_tree(left, right, root_idx, graph=None):
    if graph == None: graph = {}
    root = post_order[root_idx]
    graph[root] = [None, None]
    left_cnt = in_idx[root]-left
    right_cnt = right-in_idx[root]
    if left_cnt > 0:
        left_idx = root_idx - right_cnt - 1
        graph[root][0] = post_order[left_idx]
        make_tree(left, left+left_cnt-1, left_idx, graph)
    if right_cnt > 0:
        right_idx = root_idx-1
        graph[root][1] = post_order[right_idx]
        make_tree(left+left_cnt+1, right, right_idx, graph)
    return graph

graph = make_tree(0, n-1, n-1)

def preorder(root, result=None):
    if result == None: result = []
    result.append(root)
    if graph[root][0] != None:
        preorder(graph[root][0], result)
    if graph[root][1] != None:
        preorder(graph[root][1], result)
    return result

result = preorder(post_order[-1])
print(*result)