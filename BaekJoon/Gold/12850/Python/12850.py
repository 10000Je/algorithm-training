# no. 12850: 본대 산책2 (Gold I)
# 분할정복을 이용한 거듭제곱 문제일거란 감은 왔지만
# 결국 못풀어서 답 참고..

# 체감 난이도: Platinum V
# 사실, 인접행렬에 대해서 잘 모르면 절대 못푸는 문제라고 생각한다
# 그런 의미에서, 이 문제는 상당히 좋은 문제고, 그래프의 인접행렬 표현에 대해
# 더 깊게 알 수 있는 문제라고 생각한다.

d = int(input())
r = 1_000_000_007

def product(a, b):
    new_matrix = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                new_matrix[i][j] += (a[i][k]*b[k][j]%r)
            new_matrix[i][j] %= r
    return new_matrix

def power(a, b):
    if b == 1:
        return a
    temp = power(a, b//2)
    if b % 2 == 0:
        return product(temp, temp)
    else:
        return product(product(temp, temp), a)

_map = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

print(power(_map, d)[0][0])