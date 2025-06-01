def summation(start, end):
    return (end*(end+1))//2 + (start*(start-1))//2

s = int(input())
current_sum = 0
n = 0
while current_sum < s:
    n += 1
    current_sum = summation(1, n)
print(n if current_sum == s else n-1)