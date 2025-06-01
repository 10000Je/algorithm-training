# no. 1562: 계단 수 (Gold I)
# 백트래킹
# a에서 다음 깊이로 a+1, a-1로 가는걸 깊이 n까지 반복해서 0부터 9까지
# 모두 등장하는 계단 수를 카운트 하는 방법
# O(2^N), 하지만 문제에서 N은 100보다 작거나 같으므로, 시간초과를 피할 수 없다.
# dp 최적화 기법 적용
# 백트래킹으로 들어갈때, 현재 마지막수와 지금까지 뽑은 숫자의 개수가 동일하면
# 앞으로 나올 계단수의 조합은 동일하다
# 이때, 우리가 세야하는 것은 0부터 9까지 숫자가 모두 등장하는 계단 수인데, 이는
# 지금까지 등장한 숫자들의 조합에 종속적이다.
# 따라서, 우리는 깊이, 현재 숫자, 등장한 숫자 3가지 상태에 대해서 dp를 진행해
# 주어야 한다. -> 이때 등장한 숫자는 비트마스킹을 통해서 메모리 절약을 해볼 수 있다.
# O(10*2^10*N) -> 시간초과X

# 체감 난이도: Gold II
# 사실 외판원 순회 문제를 공부하면서, 이러한 문제가 예시로 있다 정도로
# 계단 수 문제를 보았기 때문에(물론 풀이를 보진 않았지만) dp로 바로 접근하여
# 풀 수 있었던것 같다. 그래도 dp 테이블이 3차원 까지 가는건 처음이라 조금 당황하긴
# 했지만 재밌게 풀 수 있었던 문제였다.

n = int(input())
r = 1_000_000_000
dp = [[[None for _ in range(2**10)] for _ in range(10)] for _ in range(n)]

def stair_num(depth, num, showed):
    if depth == n-1:
        if showed == (1<<10)-1:
            dp[depth][num][showed] = 1
        else:
            dp[depth][num][showed] = 0
        return dp[depth][num][showed]
    if dp[depth][num][showed] == None:
        cnt = 0
        if num + 1 <= 9:
            cnt += stair_num(depth+1, num+1, showed|(1<<(num+1)))
        if num - 1 >= 0:
            cnt += stair_num(depth+1, num-1, showed|(1<<(num-1)))
        dp[depth][num][showed] = cnt
    return dp[depth][num][showed]

cnt = 0
for i in range(1, 10):
    cnt += stair_num(0, i, 1<<i)%r
print(cnt%r)