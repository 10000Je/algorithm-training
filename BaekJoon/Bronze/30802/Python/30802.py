# no. 30802: 웰컴 키트
# 티셔츠는 같은 사이즈의 T장 묶음으로만 주문 가능
# 펜은 한 종류, P자루씩 묶음으로 주문 or 한자루씩 주문가능
# 사이즈는 S, M, L, XL, XXL, XXXL
# 티셔츠는 남아도 되지만 부족해서는 안되고 펜은 정확하게 줘야함
from math import ceil

n = int(input())
s, m, l, xl, xxl, xxxl = map(int, input().split())
t, p = map(int, input().split())

t_sum = ceil(s/t) + ceil(m/t) + ceil(l/t) + ceil(xl/t) + ceil(xxl/t) + ceil(xxxl/t)
max_p = (s+m+l+xl+xxl+xxxl) // p
cnt_p = (s+m+l+xl+xxl+xxxl) % p

print(t_sum)
print(max_p, cnt_p)