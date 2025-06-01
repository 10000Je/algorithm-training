# no. 11444: 피보나치 수 6 (Gold II)
# 피보나치 수열의 일반항을 이용하여 계산할 수 있음
# Fn = Fn-1 + Fn-2
# Fn-1 = Fn-1
# 1 1 | Fn-1 = Fn    1 1  1 1
# 1 0 | Fn-2 = Fn-1  1 0  1 0
# 1 1 의 n-1 제곱 * F1 = Fn 
# 1 0            * F0 = Fn-1
# 이 성립한다.
# 행렬의 거듭제곱을 구현하면 될듯한데 나머지 연산이 관건이다.
# 나머지 분배 법칙을 활용하면 가능

n = int(input())
r = 1_000_000_007
a = [[1, 1], [1, 0]]

def multiply_matrix(m1, m2):
    res = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            cur_sum = 0
            for k in range(len(m2)):
                cur_sum += ((m1[i][k]%r)*(m2[k][j]%r))%r
            res[i][j] = cur_sum%r
    return res

def power(n):
    if n == 1:
        return a
    temp = power(n//2)
    if n % 2:
        return multiply_matrix(multiply_matrix(temp, temp), a)
    else:
        return multiply_matrix(temp, temp)

def fib(num):
    f0, f1 = 0, 1
    if num == 0:
        return f0
    if num == 1:
        return f1
    fn = multiply_matrix(power(num-1), [[f1], [f0]])[0][0]%r
    return fn

print(fib(n))

