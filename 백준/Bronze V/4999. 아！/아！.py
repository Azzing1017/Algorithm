import sys

A = len(sys.stdin.readline().strip())
B = len(sys.stdin.readline().strip())
if A >= B:
    sys.stdout.write('go')
else:
    sys.stdout.write('no')
