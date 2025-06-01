import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = sys.stdin.readline().split()
    a_list = [char for char in a]
    b_list = [char for char in b]
    a_list.sort()
    b_list.sort()
    if a_list == b_list:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')