# e->15 s->28 m->19
e, s, m = map(int, input().split())
e = e if e != 15 else 0
s = s if s != 28 else 0
m = m if m != 19 else 0
n = s or 28
while not (n%15==e and n%28==s and n%19==m):
    n += 28 #range of s
print(n)