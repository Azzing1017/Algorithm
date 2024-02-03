import sys

N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()

sys.stdout.write('\n'.join(map(str, li)))