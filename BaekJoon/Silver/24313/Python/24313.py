a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if c-a1 > 0:
    print(1 if n0 >= a0/(c-a1) else 0)
elif c-a1 == 0:
    print(1 if a0 <= 0 else 0)
else:
    print(0)
    