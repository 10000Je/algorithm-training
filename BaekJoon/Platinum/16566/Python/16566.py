# no. 16566: 카드 게임 (Platinum V)
# 철수가 낼 카드를 입력으로 받고, 이에 민수가 낼 카드를 출력하라
# 규칙: 철수가 카드를 내면 민수는 가지고 있는 카드중 철수가 낸 카드보다
# 큰 카드 중 가장 작은 카드를 내야한다

# 일종의 그리디 알고리즘에 여러 알고리즘을 섞은 짬뽕문제다
# 카드를 정렬하면, 이분 탐색을 통해 철수의 입력보다 크면서 가장 작은
# 카드를 찾을 수 있다.
# 단, 카드는 한번만 사용할수 있기 때문에, 이미 사용한 카드는 제출할 수 없다
# 이경우, 카드를 다른 카드로 대체해야 하는데 이를 분리집합을 이용해서 진행한다
# 예를들어 5라는 카드 다음이 7이라고 할때
# 5라는 카드를 이미 냈다면 5->7 로 연결시켜주어, 5번카드를 다시 제출하려고 하면
# 7번 카드를 제출하도록 해주는 것이다
# 정리하자면, 그리디 알고리즘, 정렬, 이분 탐색, 분리집합 이 알고리즘을 적절히 
# 활용하는 문제인 것이다

# 체감 난이도: Platinum V
# 그리디 알고리즘->정렬->이분탐색->분리집합 이 일련의 사고과정이 이루어진다면
# 구현자체는 크게 어렵지 않은 문제. 단, 분리집합을 떠올리는 과정이 쉽지 않아
# 보인다. #10775 공항문제를 풀어봤다면 조금 더 쉽게 접근할 수 있는 문제

from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
cards = list(map(int, input().split()))

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    parent[root_a] = root_b

def bisect(arr, num, left=None, right=None):
    if left == None:
        left = 0
    if right == None:
        right = len(arr)-1
    if left > right:
        return left
    mid = (left+right)//2
    if num < arr[mid]:
        return bisect(arr, num, left, mid-1)
    else:
        return bisect(arr, num, mid+1, right)

cards.sort()
for num in map(int, input().split()):
    idx = bisect(cards, num)
    card = find(cards[idx])
    if card == 0:
        break
    idx = bisect(cards, card)
    if idx == len(cards):
        union(card, 0)
    else:
        union(card, cards[idx])
    print(card)