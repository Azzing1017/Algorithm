import sys

N = int(sys.stdin.readline())
li = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    li.append([x, y])
    
li.sort(key=lambda x:(x[0], x[1]))

sys.stdout.write('\n'.join(map(str, [' '.join(map(str, a)) for a in li])))