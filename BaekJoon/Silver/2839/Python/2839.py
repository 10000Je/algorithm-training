import sys

n = int(sys.stdin.readline())
five = n // 5
three = 0
while five >= 0:
    if (n - (five)*5) % 3 != 0:
        five -= 1
    else:
        three = (n - (five)*5) // 3
        break
print(five+three)