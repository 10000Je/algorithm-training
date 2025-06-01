# no. 1629: 곱셈
# a를 b번 곱한수 (a**b)를 c로 나눈 나머지
# 기본적으로 큰 문제를 작은 문제로 바꾸어 푸는 분할-정복(divide-and-conqure) 문제이다.
# a**b
# if) b가 홀수일경우
# a**b = (a**(b//2))**2 * a
# if) b가 짝수일경우
# a**b = (a**(b//2))**2
# b가 1일경우 a를 반환하면 된다.(a**1 = a)
# 나머지를 구하는 과정에서 시간초과가 나는거 같다...
# 나머지 분배 법칙을 알아야한다 ㅅㅂ
# a**(m+n) = a**m * a**n -> 지수법칙
# (a*b)%c = (a%c)*(b%c)%c -> 나머지 분배 법칙
# 이게 무슨 말이냐 하면
# a를 b로 곱한 값을 c로 나눈 나머지는
# a를 c로 나눈 나머지와 b를 c로 나눈 나머지를 곱한 값을 c로 나눈 나머지와 같다.
# 즉 두수를 c로 나눈 나머지를 곱하고, 이를 다시 c로 나눈 값과 같다는 의미이다.
# 이는 덧셈, 뺼셈, 곱셈에 적용이 된다. (나눗셈은 된다는 보장이 없음)

a, b, c = map(int, input().split())

def power(n):
    if n == 1:
        return a%c
    temp = power(n//2)
    if n % 2:
        return (temp*temp*a)%c
    else:
        return (temp*temp)%c

print(power(b))
