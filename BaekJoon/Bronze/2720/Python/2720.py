import sys

t = int(sys.stdin.readline())
for _ in range(t):
    coins = 0
    c = int(sys.stdin.readline())
    quarter = c // 25
    dime = c % 25 // 10
    nickel = c % 25 % 10 // 5
    penny = c % 25 % 10 % 5
    print(quarter, dime, nickel, penny)
    