import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
dic = {x : i for i, x in enumerate(sorted(set(arr)))}

sys.stdout.write(' '.join(map(str, [dic[x] for x in arr])))