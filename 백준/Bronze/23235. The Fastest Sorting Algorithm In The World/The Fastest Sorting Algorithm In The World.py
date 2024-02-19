import sys

cnt = 1
while True:
    x, *li = map(int, sys.stdin.readline().split())
    if len(li):
        sys.stdout.write(f"Case {cnt}: Sorting... done!"+'\n')
    else:
        break
    cnt += 1
