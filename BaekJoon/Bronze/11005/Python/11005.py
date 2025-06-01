n, b = map(int, input().split())
base = [char for char in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ']
new_num = []
while n // b:
    new_num.append(base[n%b])
    n = n // b
new_num.append(base[n])
new_num.reverse()
print(*new_num, sep='')