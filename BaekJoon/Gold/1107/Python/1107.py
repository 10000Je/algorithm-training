import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
broken_nums = set()
if m:
    for num in sys.stdin.readline().split():
        broken_nums.add(num)

min = n - 100 if 100 < n else 100 - n
count_of_number_button = 0
for i in range(0, 1000000):
    isBrokenNumHere = False
    for char in str(i):
        if char in broken_nums:
            isBrokenNumHere = True
            break
    if isBrokenNumHere:
        continue
    count_of_number_button = len(str(i))
    count_of_plus_minus = n - i if i < n else i - n
    if count_of_number_button + count_of_plus_minus < min:
        min = count_of_number_button + count_of_plus_minus
print(min)