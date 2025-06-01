import sys
import math

n = int(sys.stdin.readline())
comments = [int(sys.stdin.readline()) for i in range(n)]
comments.sort()
deleted_range = math.floor(len(comments)*0.15+0.5)
comments = comments[deleted_range:len(comments)-deleted_range]
print(math.floor(sum(comments)/len(comments)+0.5) if n != 0 else 0)
