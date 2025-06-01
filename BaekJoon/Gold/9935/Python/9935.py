# no. 9935: 문자열 폭발 (Gold IV)
# 문자열안에 폭발문자열이 존재한다.
# 문자열이 폭발 문자열을 포함하면 모든 폭발 문자열이 폭발한다.
# 남은 문자들은 순서대로 붙어서 다른 문자열이 만들어진다.
# 이 과정은 문자열 내에 더이상 폭발 문자열이 남아 있지 않을때까지 계속된다.
# 스택?
# 스택에 문자열을 쌓고 스택에 폭발문자열이 완전히 들어가면 그걸 pop 한다.
# 이 과정을 문자열 끝까지 반복하면 결국 스택에는 폭발문자열이 더이상 존재하지 않는다.

from sys import stdin
input = stdin.readline

string = input().rstrip()
tnt = input().rstrip()

stack = []
for char in string:
    stack.append(char)
    if len(stack) >= len(tnt):
        for i in range(len(tnt)):
            if stack[-1-i] != tnt[-1-i]:
                break
        else:
            for _ in range(len(tnt)):
                stack.pop()

print('FRULA' if not stack else ''.join(stack))