import sys

n1, n2 = map(int, sys.stdin.readline().split())
a = {num for num in map(int, sys.stdin.readline().split())}
b = {num for num in map(int, sys.stdin.readline().split())}

print(len(a^b))