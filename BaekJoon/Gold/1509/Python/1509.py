# no. 1509: 팰린드롬 분할 (Gold I)
# 어떤 문자열을 팰린드롬으로 분할할 때, 분할의 개수의 최소값을 구하라
# "가장 큰 팰린드롬부터 선택하여 분할하여야 개수가 최소가 될것이다." -> 그리디
# 가장 큰 팰린드롬을 기준으로 좌/우로 분할하여 재귀적으로 팰린드롬을 구해간다
# -> 분할-정복
# 반례 : BABCBABC 의경우, ABCBA, CBABC 2가지의 동일한 길이의 팰린드롬이 존재하는데
# 어느 것을 선택하느냐에 따라서, 분할의 개수가 달라진다. 즉, 그리디 알고리즘으로는 이 경우를 분간할 수 없기 때문에
# 부분해들의 최적해가 전체의 최적해가 되지 않는다. 따라서, 이는 틀렸다.

# dp
# a1~an 까지를 분할할때의 최소값은 무엇일까
# a1~an, a1/a2~an, a1~a2/a3~an ... 이중 최소값이 해당된다
# dp[i][j] -> ai~aj까지를 팰린드롬으로 분할했을때의 최소값
# dp[i][j] -> 커서를 k -> dp[i][k] + dp[k+1][j], ... 중 최소값

# tlqkf 시간초과..
# dp테이블을 만드는과정이 O(N^3)의 시간복잡도를 가지는 바람에 시간초과

# 조금 더 생각을 해보자..
# 길이가 n인 문자열을 분할한다고 해보자
# 이때 dp[n] = n번째 인덱스까지의 문자열을 분할할때의 최소값 이라고 정의해보자
# dp[n]을 구하기 위해선 무엇을 알아야할까?
# i~j까지가 팰린드롬인지 기록해놓은 테이블을 check[i][j]라고 정의해보자
# check[0][n-1], check[1][n-1] ... 까지 확인을 하는데
# 이때 만약 check[i-1][n-1]이 팰린드롬이라고 해보자
# 우리는 dp테이블의 값을 갱신시켜주어야 한다
# i번째 부터 n-1번째까지의 문자열이 팰린드롬이므로 우리는 이를 하나의 덩어리로
# 분리할 수 있다는 의미이다. 즉, 이렇게 나눌 경우의 분리횟수는
# i-1번째까지의 최소분리횟수(dp[i-1])에 1을 더한 값이다.
# dp[n]은 여러 경우의 수중 최소값을 가져야 하므로 min()함수를 통해 최소가 될때만
# 갱신시켜주어야 한다
# dp[n] = min(dp[n], dp[i-1]+1)

# 체감 난이도: G1
# 2가지의 dp를 사용해야 한다는 점이 매우 어려웠습니다.
# 아이디어를 떠올리는 수준이 절대 골드가 아니고 맘같아선 플레5를 주고싶다.

from math import inf

string = input()
n = len(string)
check = [[False for _ in range(n)] for _ in range(n)]

for i in range(2*n-1):
    if i%2==0:
        left = right = i//2
    else:
        left = i//2
        right = left + 1
    while string[left] == string[right]:
        check[left][right] = True
        left -= 1
        right += 1
        if left < 0 or right >= n:
            break

dp = [inf for _ in range(n+1)]
dp[0] = 0
dp[1] = 1
for i in range(2, n+1):
    for j in range(1, i+1):
        if check[j-1][i-1]:
            dp[i] = min(dp[i], dp[j-1]+1)
print(dp[n])