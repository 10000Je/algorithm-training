import sys

str1 = sys.stdin.readline().rstrip()
str1 = str1.replace('c=', 'c')
str1 = str1.replace('c-', 'c')
str1 = str1.replace('dz=', 'd')
str1 = str1.replace('d-', 'd')
str1 = str1.replace('lj', 'l')
str1 = str1.replace('nj', 'n')
str1 = str1.replace('s=', 's')
str1 = str1.replace('z=', 'z')
print(len(str1))