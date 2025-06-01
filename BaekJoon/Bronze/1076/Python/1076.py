c1 = input()
c2 = input()
c3 = input()

val = {
    'black': 0, 'brown': 1, 'red': 2, 
    'orange': 3, 'yellow': 4, 'green': 5, 
    'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}
r = (10*val[c1] + val[c2]) * 10**val[c3]
print(r)