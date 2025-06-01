# no. 20303: 할로윈의 양아치 (Gold III)
# 1) 친구의 친구는 친구다. (친구끼리 그룹으로 연결되어 있다.)
# 2) 스브러스는 k명 미만의 애들 한에서 사탕을 뜯어야 한다.
# 각 그룹은 구성원의 수 w와 사탕의 개수 v를 갖는다.
# 문제에서는, 최대 n개의 그룹들 속에서, 여러 그룹을 골라 구성원의 수의 합이 k미만이 되도록
# 담아, 사탕의 개수가 최대가 되도록 담으라고 한다.
# 이 문제는 배낭문제의 변형이다!! -> BFS/DFS + knapsack 혼합문제

# 체감 난이도: Gold II
# 문제가 좀 애매해서 사실 BFS/DFS만 떠올릴수 있다면 배낭까진 쉽게 떠올릴 수 있다.
# 단, 여러 알고리즘의 혼합이라는 요소 때문에 Gold II 는 줘야하지 않나 생각

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

n, m, k = map(int, input().split())
nums = (0,) + tuple(map(int, input().split()))

graph = {i: set() for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

check = [0 for _ in range(n+1)]
def dfs(cur_node, num, visited=None):
    if visited==None: visited = set()
    check[cur_node] = num
    visited.add(cur_node)
    cnt = nums[cur_node]
    for near_node in graph[cur_node]:
        if near_node in visited:
            continue
        cnt += dfs(near_node, num, visited)[1]
    return len(visited), cnt

w = [0]
v = [0]
idx = 1
for i in range(1, n+1):
    if check[i] == 0:
        a, b = dfs(i, idx)
        w.append(a)
        v.append(b)
        idx += 1

dp = [[0 for _ in range(k)] for _ in range(idx)]
for i in range(1, k):
    for j in range(1, idx):
        if w[j] > i:
            dp[j][i] = dp[j-1][i]
        else:
            dp[j][i] = max(dp[j-1][i], dp[j-1][i-w[j]]+v[j])

print(dp[idx-1][k-1])