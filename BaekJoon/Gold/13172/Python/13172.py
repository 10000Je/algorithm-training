# no. 13172: Σ (Gold IV)
# 이 문제를 풀기위해서...
# 유클리드 알고리즘(gcd), 확장 유클리드 알고리즘(xgcd)
# 베주 항등식, 모듈러 연산, 모듈러 나눗셈의 방법
# 모듈러 곱셈의 역원 구하는 법(+페르마의 소정리)
# 을 알아야한다.
# 사실 페르마의 소정리와 모듈러 연산만 알아도 되지만 위의 개념을 익힐수 있는
# 기회가 되어주는 문제
# 문제를 푸는 방법은 베주 항등식과 확장 유클리드 알고리즘을 이용하는 방법과
# 페르마의 소정리를 이용하는 방법이 있다. (나는 페르마의 소정리를 이용하려 한다.)
# a^p = a (mod p), 이때 p는 소수이다.

from sys import stdin
input = stdin.readline
r = 1_000_000_007

m = int(input())
dices = tuple(tuple(map(int, input().split())) for _ in range(m))

def power(a, b):
    if b == 1:
        return a%r
    temp = power(a, b//2)
    if b % 2:
        return ((temp%r)*(temp%r)*(a%r))%r
    else:
        return ((temp%r)*(temp%r))%r

ans = 0
for i in range(m):
    n, s = dices[i]
    ni = power(n, r-2)
    ans = (ans + (s*ni)%r)%r

print(ans)