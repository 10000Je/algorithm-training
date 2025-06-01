import sys

n, m = map(int, sys.stdin.readline().split())
nameToNumber = {}
numberToName = {}
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    nameToNumber[name] = i
    numberToName[i] = name
for i in range(0, m):
    pokemon = sys.stdin.readline().rstrip()
    if pokemon in nameToNumber:
        print(nameToNumber[pokemon])
    else:
        print(numberToName[int(pokemon)])