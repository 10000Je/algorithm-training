str1 = input()

def get_h(dishes):
    if len(dishes) == 1:
        return 10
    cur_dish = dishes[-1]
    last_dish = dishes[-2]
    if cur_dish == last_dish:
        return 5 + get_h(dishes[:-1])
    else:
        return 10 + get_h(dishes[:-1])

print(get_h(str1))