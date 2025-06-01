import sys

foundFBI = False
for i in range(0,5):
    if 'FBI' in sys.stdin.readline().rstrip():
        print(i+1, ' ', sep='', end='')
        foundFBI = True
if foundFBI == False:
    print('HE GOT AWAY!')