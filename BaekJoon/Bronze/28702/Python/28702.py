# no. 28702: FizzBuzz (Bronze I)
# 피즈버즈 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어진다.
# 다음으로 출력될 수 있는 문자열을 출력하라
# 답이 여러개면 아무거나 출력하라
# 생각해보자, 세개의 문자열이 출력된다면 적어도 셋 중 하나는 3의 배수일 것이다
# 셋 중 두 수는 3의 배수가 아닐 것이다
# 셋 중 5의 배수는 하나만 존재할 수 있다. (아니면 없거나)
# 그렇다면, 적어도 한 수는 "숫자"로 출력됨이 보장되어 있다

a = input()
b = input()
c = input()

if a not in {'Fizz', 'Buzz', 'FizzBuzz'}:
    num = int(a)+3
elif b not in {'Fizz', 'Buzz', 'FizzBuzz'}:
    num = int(b)+2
else:
    num = int(c)+1

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(num)