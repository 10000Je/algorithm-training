import sys

t = int(sys.stdin.readline())
for _ in range(t):
    words = sys.stdin.readline().split()
    new_words = [word[::-1] for word in words]
    print(*new_words)