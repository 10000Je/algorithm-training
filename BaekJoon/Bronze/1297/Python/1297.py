import sys
import math

d, h, w = map(int, sys.stdin.readline().split())
x = math.sqrt((d*d) / (h*h + w*w))
print(int(h*x), int(w*x), sep=' ') 
