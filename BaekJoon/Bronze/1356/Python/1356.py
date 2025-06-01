n = input()
for i in range(1, len(n)):
    a, b = n[:i], n[i:]
    a_mul = 1
    for num in a:
        num = int(num)
        a_mul *= num
    b_mul = 1
    for num in b:
        num = int(num)
        b_mul *= num
    if a_mul == b_mul:
        print('YES')
        break
else:
    print('NO')    