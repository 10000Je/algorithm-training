# no. 16724: 피리 부는 사나이 (Gold III)
# 성우가 설정한 방향 지도가 주어졌을 때, 재훈이를 도와서 영과일 회원들이
# 지도 어디에 있는 safezone으로 이동할 수 있도록 배치할 수 있는 safezone의
# 최소 개수를 구하라
# 그리디 알고리즘, 분리집합

# 먼저, 화살표를 통해 연결된 모든 칸들은 하나의 그룹으로 간주할 수 있다.
# 화살표를 통해 연결된 칸 예를 들어, a->b->c->d 칸 순으로 연결되어 있을때
# abcd의 모든 칸들은 최종 종점인 d로 이동할 수 있다.
# 즉, 그룹내의 종점이 safezone이라면, 그룹내의 모든 정점에서 safezone으로 이동하는 것이
# 가능하다. 최소개수는 그룹의 개수가 되며(그리디 알고리즘), 그룹은 분리집합(union-find)을
# 통해 구할 수 있다.

# 체감 난이도: Gold III
# 분리집합을 떠올리면 쉬운문제, 모든 정점에 대해서 union-find을 실행해주고
# 마지막으로 모든 정점에 find()연산을 실행해 경로압축을 진행해주면 풀리는 문제
# 그리 어렵지는 않음

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
input = stdin.readline

n, m = map(int, input().split())
_map = tuple(tuple(input().rstrip()) for _ in range(n))

parent = [[(i, j) for j in range(m)] for i in range(n)]

def find(x):
    r, c = x
    if parent[r][c] != (r, c):
        parent[r][c] = find(parent[r][c])
    return parent[r][c]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    r1, c1 = root_a
    r2, c2 = root_b
    parent[r2][c2] = (r1, c1) 

for r in range(n):
    for c in range(m):
        direction = _map[r][c]
        dr, dc = r, c
        if direction == "U":
            dr -= 1
        if direction == 'D':
            dr += 1
        if direction == 'L':
            dc -= 1
        if direction == 'R':
            dc += 1
        if (0 <= dr < n) and (0 <= dc < m):
            root_a = find((r, c))
            root_b = find((dr, dc))
            if root_a == root_b:
                continue
            union(root_a, root_b)

for r in range(n):
    for c in range(m):
        find((r, c))

cnt = set()
for r in range(n):
    for c in range(m):
        cnt.add(parent[r][c])

print(len(cnt))