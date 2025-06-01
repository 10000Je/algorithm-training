import sys

l, p, v = map(int, sys.stdin.readline().split())
idx = 1
while l or p or v:
    print(f'Case {idx}: {(v//p)*l+min(l, v%p)}')
    l, p, v = map(int, sys.stdin.readline().split())
    idx += 1