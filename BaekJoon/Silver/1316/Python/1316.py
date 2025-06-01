import sys

def isGroundWord(word):
    memo = {}
    last_char = None
    for char in word:
        if char in memo:
            if last_char != char:
                return False
        else:
            memo[char] = True
        last_char = char
    return True

n = int(sys.stdin.readline())
count = 0
for i in range(n):
    str1 = sys.stdin.readline().rstrip()
    if isGroundWord(str1):
        count += 1
print(count)