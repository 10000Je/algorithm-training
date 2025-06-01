import sys

def is_palindrome(string, cnt=1):
    if len(string) <= 1:
        return (1, cnt)
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1], cnt+1)
    else:
        return (0, cnt)

t = int(sys.stdin.readline())
for _ in range(t):
    cur_str = sys.stdin.readline().rstrip()
    r, c = is_palindrome(cur_str)
    print(r, c)