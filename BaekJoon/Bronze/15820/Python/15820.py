# no. 15820: 맞았는데 왜 틀리죠?

from sys import stdin
input = stdin.readline

s1, s2 = map(int, input().split())
sample = system = True
for _ in range(s1):
    a, b = map(int, input().split())
    if a != b:
        sample = False
for _ in range(s2):
    a, b = map(int, input().split())
    if a != b:
        system = False

if sample == True and system == True:
    print("Accepted")
elif sample == False:
    print("Wrong Answer")
else:
    print("Why Wrong!!!")