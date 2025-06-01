import sys
import re

while True:
    try:
        str_1 = input()
        small = len(re.findall('[a-z]', str_1))
        big = len(re.findall('[A-Z]', str_1))
        num = len(re.findall('[0-9]', str_1))
        space = len(re.findall(' ', str_1))
        print(small, big, num, space)
    except EOFError:
        break