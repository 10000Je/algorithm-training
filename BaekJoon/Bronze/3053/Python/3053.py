from math import pi

def euclid(r):
    return (r**2)*pi

def taxi(r):
    return (r**2)*2.0

r = int(input())
print(f'{euclid(r):.6f}')
print(f'{taxi(r):.6f}')