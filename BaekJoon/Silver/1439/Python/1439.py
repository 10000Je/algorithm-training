import re

s = input()
zero = re.compile('0+')
one = re.compile('1+')
print(min(len(zero.findall(s)), len(one.findall(s))))