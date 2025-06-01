# no. 11049: 행렬 곱셈 순서 (Gold III)
# 처음엔 그리디로 해결하려 했으나, 최적해가 된다는 보장이 없어서 실패
# 알고리즘 힌트 보고 dp로 접근시도

# 행렬 a1, a2, a3, ..., an 이 존재한다
# a1부터 an까지의 행렬곱을 mn이라고 해보자
# 행렬의 곱은 교환법칙은 성립하지 않지만 결합법칙은 성립한다. 즉,
# 괄호로 묶어서 계산할 수 있으며 이 괄호가 바로 이 문제의 부분문제에 속한다.
# 행렬곱 ABC는 (AB)C 또는 A(BC)로 해결되며 이때 AB와 BC가 ABC의 부분문제인 것이다

# 하지만 이런 부분문제가 단순히 정의되지 않는 것이 이 문제의 어려움이다.
# ABCD는 A(BCD), (AB)(CD), (ABC)D 세가지로 나뉜다
# A(BC)D이런 경우는, (ABC)D 나 A(BCD) 둘중 하나의 경우로 구별이 된다 그래서고려X

# 후기->dp는 진짜진짜 아이디어가 전부인 문제다
# 솔직히 아이디어 이거? 혼자 떠올리라고 하면 3일을 줘도 못할거같다
# 행렬곱셈의 순서가 대체 왜 dp로 풀릴수 있는지도 모르겠고 사실
# 직접 고민해봤을때 어..이거 되나? 아ㅏㄴ되는데.. 이딴 생각만 계속들고
# 진짜 진짜... 이게 뭐냐 대체...
# 체감난이도는 거의 뭐 ㅅㅂ 난 지금 플레4문제는 풀고있는줄 알았다
# 위상정렬, 최소스패닝트리 이딴 이름도 이상한 알고리즘은 ㅈㄴ 쉬운데
# dp는 순수하게 수학 수능 21번 푸는느낌이라 존나 개빡친다 그냥

# 심지어 이문제는 정해로 풀어도 시간복잡도 빡센문제라 바텀-탑 방식아니면
# python3 제출로는 풀지도 못한다.
# 어떤게 이딴 문제가 정답률 43% 인지도 모르겠고, 그냥 ㅈㄴ 어이가 없다 ㅋㅋ

# 배운점 -> 메모이제이션은 왠만하면 배열을 사용하자 (ex, 2차원 배열)
# 메모이제이션 기법을 바꾸니 pypy3에선 통과되더라
# 시간복잡도 -> O(N^3)

from sys import stdin
input = stdin.readline

n = int(input())
sizes = tuple(tuple(map(int, input().split())) for _ in range(n))
inf = 2**31

def moc(st, ed, dp=None):
    if dp == None:
        dp = [[inf for _ in range(500)] for _ in range(500)]
    if st == ed:
        if dp[st][ed] == inf:
            dp[st][ed] = 0 
        return dp[st][ed]
    else:
        if dp[st][ed] == inf:
            for k in range(st, ed):
                dp[st][ed] = min(dp[st][ed], moc(st, k, dp)+moc(k+1, ed, dp)+sizes[st][0]*sizes[k][1]*sizes[ed][1])
        return dp[st][ed]

print(moc(0, n-1))