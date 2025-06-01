# no. 1918: 후위 표기식 (Gold II)
# 중위 표기식을 후위 표기식으로 바꾸어라

# A*(B+C*D+E/F)
# A*(BCD*+EF/+)
# ABCD*+EF/+*

# 이 문제의 핵심은
# "언제 스택에 넣고, 언제 스택에서 팝하는가"
# 후위연산의 특징. -> 한 연산에서 무조건 피연산자가 연산자보다 먼저 출력된다.
# 피연산자는 stack에 넣지않고 바로바로 출력하고
# 연산자를 언제 출력할지를 정하는게 이 문제의 핵심이다.

string = input()
stack = []
priority = {'*': 1, '/': 1, '+': 0, '-': 0}
for char in string:
    if char in {'*', '/', '+', '-'}:
        if not stack or stack[-1] == '(' or priority[char] > priority[stack[-1]]:
            stack.append(char)
        else:
            while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[char]:
                output = stack.pop()
                print(output, end='')
            stack.append(char)
    elif char == ')':
        output = stack.pop()
        while output != '(':
            print(output, end='')
            output = stack.pop()
    elif char == '(':
        stack.append(char)
    else:
        print(char, end='')
while stack:
    print(stack.pop(), end='')
print()
