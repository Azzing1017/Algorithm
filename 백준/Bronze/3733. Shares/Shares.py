import sys
lines = sys.stdin.readlines()
li = [int(y) // (int(x) + 1) for x, y in (line.strip().split() for line in lines)]

sys.stdout.write('\n'.join(map(str, li)))
