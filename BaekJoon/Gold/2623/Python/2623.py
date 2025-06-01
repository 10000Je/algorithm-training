# no. 2623: 음악프로그램 (Gold III)
# 위상정렬 문제
# 단, 싸이클이 존재해서 순서를 판정할 수 없음을 판단해야한다

# 한가지 조건을 생각해야 한다
# 다른 보조 PD가 중복되는 순서로 순서를 정해오는 것이 가능하다
# 중복된 간선은 그래프에 추가하지 않아야 하는데, 처리 과정에서 진입차수가 증가하는 문제가
# 발생한다

# 체감 난이도: Gold IV
# 체감 난이도는 원래 Gold V 정도였지만, 약간의 함정이 숨어 있는 문제여서 Gold IV로 정했다
# 위상정렬을 할 줄 안다면 쉽게 풀 수 있는 문제이다.

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
graph = {i: set() for i in range(1, n+1)}
in_order = [0 for _ in range(n+1)]

for _ in range(m):
    orders = tuple(map(int, input().split()))
    for i in range(1, len(orders)-1):
        if orders[i+1] in graph[orders[i]]: continue
        graph[orders[i]].add(orders[i+1])
        in_order[orders[i+1]] += 1

def topology_sort():
    stack = [i for i in range(1, n+1) if in_order[i]==0]
    result = []
    while stack:
        cur_singer = stack.pop()
        result.append(cur_singer)
        for next_singer in graph[cur_singer]:
            in_order[next_singer] -= 1
            if in_order[next_singer] == 0:
                stack.append(next_singer)
    if len(result) != n:
        return None
    else:
        return result

result = topology_sort()
if result == None:
    print(0)
else:
    print(*result, sep='\n')