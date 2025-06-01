# no. 11304: 캥거루 세머리2
from sys import stdin
input = stdin.readline

_str = input().rstrip()
while _str:
    a, b, c = map(int, _str.split())
    print(max(abs(a-b), abs(b-c))-1)
    _str = input().rstrip()