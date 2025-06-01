# no. 2098: 외판원 순회 (Gold I)
# n개의 도시를 순회하는 최소비용을 구하라
# 최단거리 알고리즘 -> 모든 도시를 순회한다는 보장이 없다.
# 백트래킹
# 지금까지 방문한 정점과 현재정점을 이용하여 백트래킹을 통해 완전탐색을 시도
# 시간복잡도가 n! 이므로, 시간초과로 인해 실패하였음 (n<=16)
# ...-> 알고리즘 분류 봄
# 비트필드를 이용한 dp? -> 이문제는 dp로 설계해야함

# 생각해보자, 현재 방문중인 정점과, 지금까지 방문한 정점이 같다면, 남은 점들을
# 순회하고 돌아오는 최소거리는 정해져 있지 않을까?
# 즉, 1번부터 5번까지 순회하고 1번으로 돌아온다고 가정해보자
# 1->2->3->4 을 상태1 이라하고, 1->3->2->4 을 상태2 이라 해보자
# 여기서 4번정점에서 "나머지 정점들"을 순회하고 돌아오는 거리는 
# 두 상태모두 5->1 으로 동일하다
# 왜냐면 지금까지 방문한 정점과 현재 위치하고 있는 정점이 같다는 의미는
# 앞으로 방문할 수 있는 정점들의 경우의 수가 동일하다는 의미이기 때문이다

# 그렇다면 dp 테이블에 이러한 정보를 저장할 수 있지 않을까?
# dp[현재정점][방문한정점들] = 현재 정점에서 방문하지 않은 나머지 정점들을 방문하고
# 돌아오는데 걸리는 비용(처음부터 현재 정점까지 방문하는데 걸린 비용을 제외한 값)
# 왜냐면 "지금까지의 경로"가 어찌되었든, 저 dp 테이블에 저장된 값은 변경되지 않고 계속
# 사용될 것이기 때문이다.
# 즉, 중복된 경로를 다시 탐색하지 않아도 되는 것이다
# 시간복잡도는 dp 테이블의 크기 n*(2^n) 만큼 함수의 호출이 발생하고
# 매 함수의 호출마다 n개의 정점으로의 경로가 존재하는지 탐색하므로
# O(N^2*(2^N))이 된다. N <= 16 이므로, 시간복잡도 조건을 충족한다. 약, 16777216

# 추가적으로 여기에 비트마스킹 기법의 최적화가 이루어 질 수 있다.
# 방문한정점들의 상태는 2^N개 존재한다. 이는 단순히 n개의 원소를 담을 수 있는
# set을 통해 구현할 수 있으며, 이는 비트연산을 통해 하나의 숫자로 구현이 가능하다
# 이 방법을 사용하면 set에서 시간에서의 우위를 가져갈 수 있다. 덤으로 메모리 절약도 가능

# dp 테이블 갱신시, 만약 돌아오는 경로가 존재하지 않는다면, inf를 반환하여 경로가 없음을
# 나타내자

# 체감 난이도: P5
# 이 문제가 골드1을 받을 수 있는 유일한 이유는, 유명하기 떄문이라고 감히 말할 수 있다
# 백트래킹에서의 dp를 이용한 최적화 적용은 한번 경험해 보지 않는 이상 추론으로
# 떠올리기 매우어렵고, 설령 이 아이디어를 떠올려도 그 해법을 스스로 찾는 것은 더욱
# 어렵다. 만약 알고리즘 분류도 안보고 풀었으면 며칠은 이 문제로 머리를 싸매고 있지 않았을까

from sys import stdin
from math import inf
input = stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

def tsp(start, cur_city=None, visited=None, dp=None):
    if dp == None: dp = [[None for _ in range(2**n)] for _ in range(n)]
    if cur_city == None: cur_city = start
    if visited == None: visited = 1 << start
    if (1 << n)-1 == visited:
        if w[cur_city][start]:
            dp[cur_city][visited] = w[cur_city][start]
        else:
            dp[cur_city][visited] = inf
        return dp[cur_city][visited]
    if dp[cur_city][visited] == None:
        min_cost = inf
        for i in range(n):
            if w[cur_city][i] and visited & (1 << i) == 0:
                min_cost = min(min_cost, w[cur_city][i]+tsp(start, i, visited|(1 << i), dp))
        dp[cur_city][visited] = min_cost
    return dp[cur_city][visited]

print(tsp(0))