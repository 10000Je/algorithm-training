n = int(input())
max_num = 0
for i in range(n+1):
    for char in str(i):
        if int(char) != 4 and int(char) != 7:
            break
    else:
        max_num = i
print(max_num)