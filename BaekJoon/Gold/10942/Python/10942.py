# no. 10942: 팰린드롬? (Gold IV)
# 매번 확인히는 방법 -> 2000 * 1_000_000 -> 시간초과
# 수열의 한 지점을 "중간수(middle)"으로 지정함으로써
# 두개의 포인터를 이용하여 하나는 매번 감소, 하나는 증가시킴으로써
# 한 숫자를 중간수로 지정할때마다 O(N)안에 S, E에 대한 팰린드롬 여부를 저장할 수 있고
# 모든 숫자를 중간수로 지정했을때 모든 경우의 S, E에 대한 팰린드롬 여부를 알 수 있다
# 따라서 팰린드롬 여부를 O(N^2) 시간안에 저장가능하고
# 저장된 값을 불러오는 작업은 O(1)시간을 소요하니 시간복잡도를 맞출 수 있다
# 이때 중간수는 빈 공간도 포함해야한다 그래야 두개로 이루어진 숫자의 팰린드롬 여부도 판별가능

# 후기,
# 나는 이문제를 dp로 안풀고 조금 특이한 방식으로 접근해서 투포인터로 풀어냈다
# dp로 푸는 해법도 보면 좋을 것 같다
# 무엇보다 스스로 알고리즘 힌트를 안보고 나만의 해법으로 정해로 풀어낸 것이 너무 뿌듯하다.

from sys import stdin
input = stdin.readline

n = int(input())
nums = tuple(map(int, input().split()))

is_palindrome = [[None for _ in range(n)] for _ in range(n)]

for mid in range(2*n-1):
    left = right = None
    if mid % 2 == 0:
        left = right = (mid // 2)
    else:
        left = mid // 2
        right = left + 1

    is_still_palindrome = True
    while left >= 0 and right < n:
        if nums[left] == nums[right] and is_still_palindrome:
            is_palindrome[left][right] = 1
        else:
            is_palindrome[left][right] = 0
            is_still_palindrome = False
        left -= 1
        right += 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(is_palindrome[s-1][e-1])
