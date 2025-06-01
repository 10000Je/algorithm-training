# no. 2162: 선분 그룹 (Platinum V)
# n개의 선분들이 주어졌을 때, 이 선분들은 총 몇개의 그룹으로 되어 있을까?
# 또, 가장 크기가 큰 그룹에 속한 선분의 개수는 몇 개 일까? 를 구하시오
# 그룹: 두 선분이 서로 만나는 경우(교차)에, 두 선분은 같은 그룹에 속함
# -> 분리집합, 기하학(선분교차)응용 문제

# 체감 난이도: Gold I
# 선분교차에서 많은 실수가 나올 수 있는것에 주의한다면 쉽게 풀 수 있는 문제
# 분리집합 아이디어를 떠올리는 것은 사실 분리집합이 무엇인지만 안다면
# 그렇게 어렵지는 않음.

from sys import stdin
input = stdin.readline

n = int(input())

def loc_vector(start, end):
    x1, y1 = start
    x2, y2 = end
    return (x2-x1, y2-y1)

def outer_product(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1*y2) - (x2*y1)

def is_crossed(a, b):
    x1, y1, x2, y2 = a
    x3, y3, x4, y4 = b
    op1 = outer_product(loc_vector((x1, y1), (x2, y2)), loc_vector((x1, y1), (x3, y3)))
    op2 = outer_product(loc_vector((x1, y1), (x2, y2)), loc_vector((x1, y1), (x4, y4)))
    op3 = outer_product(loc_vector((x3, y3), (x4, y4)), loc_vector((x3, y3), (x1, y1)))
    op4 = outer_product(loc_vector((x3, y3), (x4, y4)), loc_vector((x3, y3), (x2, y2)))
    if op1 * op2 > 0:
        return False
    elif op1 * op2 == 0:
        if op3 * op4 > 0:
            return False
        elif op3 * op4 < 0:
            return True
        else:
            if abs(x2-x1) + abs(x4-x3) < abs(max(x1, x2, x3, x4) - min(x1, x2, x3, x4)):
                return False
            if abs(y2-y1) + abs(y4-y3) < abs(max(y1, y2, y3, y4) - min(y1, y2, y3, y4)):
                return False
            return True
    else:
        if op3 * op4 > 0:
            return False
        else:
            return True

lines = tuple(tuple(map(int, input().split())) for _ in range(n))
parent = [i for i in range(len(lines))]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a

cnt = {}

for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            continue
        if find(i) == find(j):
            continue
        a = lines[i]
        b = lines[j]
        if is_crossed(a, b):
            union(i, j)

for num in parent:
    if num not in cnt:
        cnt[num] = 1
    else:
        cnt[num] += 1

print(len(cnt))
print(max(cnt.values()))