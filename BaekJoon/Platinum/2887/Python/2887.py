# no. 2887: 행성 터널 (Platinum V)
# n개의 행성을 최소거리로 연결하는 최소 스패닝 트리를 그려라
# 단, 입력으로는 간선이 주어지지 않으며, 각 정점의 위치가 주어진다
# 두 정점을 있는 간선의 길이는 min(|xa-xb|, |ya-yb|, |za-zb|)이다.

# 간선이 주어지지 않으므로 직접 만들어야한다
# n이 10만까지 가능하므로, 모든 정점에 대한 간선을 다 체크한다면 시간초과임
# 최소 스패닝 트리를 이루는 간선들의 특징을 생각해 볼 필요가 있다.
# 최소 스패닝 트리를 구하는 알고리즘 중에 프림 알고리즘이라는 것이 있다.
# 이 알고리즘은, 한 정점부터 시작하여 "가장 인접한 정점"을 찾아가며 최소 스패닝 트리를
# 그리는데, 이는 최소 스패닝 트리를 이루는 간선은 가장 인접한 정점을 잇고있음을 의미한다
# 즉, 한 정점의 가장 인접한 정점에 대한 간선들만이 최소 스패닝 트리에 포함된다는 것을
# 알 수 있다.

# 즉, 가장 인접한 정점을 잇는 간선들만이 최소 스패닝 트리에 포함 될 수 있다는 사실과
# 문제에서 정의한 거리는, x의 거리, y의 거리, z의 거리중 최소값이므로, 우리는 x에 대해 인접한 정점의 간선
# y에 대해 인접한 정점의 간선, z에 대해 인접한 정점의 간선을 구해야한다
# 여기서, 그러면 같은 정점에 대한 여러 간선이 생길 수 있는데, 크루스칼 알고리즘을 사용하면, 가중치가 최소인 간선부터 채택하므로
# 같은 두 정점에 대한 여러 간선이 있을 경우, 알아서 최소 가중치의 간선을 선택할 수 있다.
# O(N)

# 체감 난이도: P5
# 아이디어를 떠올리는 것이 너무 힘들고, 어떻게 간선들을 가지치기 해야하는지 아이디어를 얻는게
# 너무 힘들었다. 결국 인터넷에 검색하여 풀이를 보았음에도 처음 보았을때 이해하는 데까지 몇시간이 걸렸으며
# 최소 스패닝 트리를 구하는 방법들을 다시한번 복습할 수 있는 기회가 되었고, 최소 스패닝 트리를 그리는
# 원리를 더 깊이 이해할 수 있었던 문제이다.
# 핵심은, 인접한 정점 이외의 간선을 선택해선, 절대 최소 스패닝 트리를 만들 수 없다는 것을
# 인지하는 것이다. 애초에 인접한 정점 이외의 간선도 필요가 없다.

from sys import stdin
input = stdin.readline

n = int(input())
dots = tuple(tuple(map(int, input().split())) for _ in range(n))
edges = []

x = [i for i in range(n)]
x.sort(key=lambda x:dots[x][0])
for i in range(n-1):
    a, b = x[i], x[i+1]
    edges.append((a, b, abs(dots[a][0]-dots[b][0])))

x.sort(key=lambda x:dots[x][1])
for i in range(n-1):
    a, b = x[i], x[i+1]
    edges.append((a, b, abs(dots[a][1]-dots[b][1])))

x.sort(key=lambda x:dots[x][2])
for i in range(n-1):
    a, b = x[i], x[i+1]
    edges.append((a, b, abs(dots[a][2]-dots[b][2])))

edges.sort(key=lambda x:x[2])

parent = [i for i in range(n)]
rank = [0 for _ in range(n)]

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1

mst = 0
for edge in edges:
    a, b, cost = edge
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        continue
    mst += cost
    union(root_a, root_b)

print(mst)