import sys

n = int(sys.stdin.readline())
memo = {sys.stdin.readline().rstrip() for _ in range(n)}
for word in memo:
    if word[::-1] in memo:
        print(len(word), word[len(word)//2])
        break