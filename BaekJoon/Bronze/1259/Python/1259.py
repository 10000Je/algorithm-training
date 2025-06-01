import sys

def isPalindrome(string):
    left = 0
    right = len(str)-1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

str = sys.stdin.readline().rstrip()
while str != '0':
    if isPalindrome(str):
        print('yes')
    else:
        print('no')
    str = sys.stdin.readline().rstrip()