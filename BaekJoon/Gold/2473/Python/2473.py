# no. 2473: 세 용액 (Gold III)
# 투포인터 심화문제
# n개의 용액을 정렬한다
# n개의 용액중 하나를 택하고, 이 용액의 특성값이 c라고 해보자.
# 이제 나머지 2개의 용액을 적절히 선택해서 세 용액의 특성합이 가장 0에 가깝도록 
# 숫자를 고른다.
# 단 이때, 가장 0에 가까운 세 숫자 조합이 존재할때, 우리가 처음에 선택한 숫자가
# 포함되리라는 보장이 없기 때문에, n개의 용액에 대하여 위의 알고리즘을 반복해야한다.
# O(N^2)

# 체감 난이도: Gold III
# 투포인터의 아이디어를 떠올리는 건 어렵지 않지만, 그래도 세 용액을 고르라는 것에서
# 당황하기 쉬운 문제였다고 생각한다. 찬찬히 고민하면 풀 수 있는 문제

from sys import stdin
input = stdin.readline

n = int(input())
sol = list(map(int, input().split()))
sol.sort()

min_comb = [sol[0], sol[1], sol[2]]
for i in range(n):
    j = 0 if i != 0 else 1
    k = n-1 if i != n-1 else n-2
    while j < k:
        if abs(sol[i]+sol[j]+sol[k]) < abs(sum(min_comb)):
            min_comb = [sol[i], sol[j], sol[k]]
        if sol[i]+sol[j]+sol[k] > 0:
            k -= 1
            if k == i:
                k -= 1
        elif sol[i]+sol[j]+sol[k] < 0:
            j += 1
            if j == i:
                j += 1
        else:
            min_comb = [sol[i], sol[j], sol[k]]
            break  

min_comb.sort()
print(*min_comb)