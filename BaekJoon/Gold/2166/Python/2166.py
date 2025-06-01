# no. 2166: 다각형의 면적 (Gold V)
# 처음 풀어보는 기하학 문제라서 많이 해멨다
# 다각형은 삼각형들의 집합으로 쪼갤수 있다
# 삼각형의 넓이는 삼각형을 이루는 두 선분의 외적으로 구할 수 있다.
# 주의해야 하는 점은, 다각형이 항상 볼록한 것이 아닌, 오목할 수 있다는 것이다.
# 이 때문에, 우리는 외적의 크기만 고려하는 것이 아니라, 외적의 부호까지 고려해야한다.

# 체감 난이도: G2
# 기하학은 풀어본적이 없어서 체감상 어려웠던 것 같다.
# 기본적으로 벡터의 외적개념이 핵심이 되는 문제
# 특히, 도형이 오목한 경우에도 왜 외적이 가능한지 직관적으로 알기 힘들어서
# 머리를 많이 쓴 문제이다.

from sys import stdin
input = stdin.readline

n = int(input())
points = tuple(tuple(map(int, input().split())) for _ in range(n))

def outer_product(a, b):
    x1, y1 = a
    x2, y2 = b
    return (x1*y2)-(y1*x2)

base_point = points[0]
def loc_vector(a):
    x, y = a
    x -= base_point[0]
    y -= base_point[1]
    return (x, y)

area = 0
for i in range(1, n-1):
    a = loc_vector(points[i])
    b = loc_vector(points[i+1])
    area += outer_product(a, b)

area *= (0.5)
print(abs(area))