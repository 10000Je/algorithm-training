import sys

k, n = map(int, sys.stdin.readline().split())
arr1 = []
for i in range(0, k):
    arr1.append(int(sys.stdin.readline()))
left_boundary = 1
right_boundary = (2**31)-1
middle_point = None
max = 0
while left_boundary <= right_boundary:
    middle_point = (left_boundary + right_boundary) // 2
    num_of_pieces = 0
    for num in arr1:
        num_of_pieces += (num // middle_point)
    if num_of_pieces < n:
        right_boundary = middle_point-1
    else:
        left_boundary = middle_point+1
        if middle_point > max:
            max = middle_point
print(max)
