import sys

res = 0
for _ in range(5):
    res += int(sys.stdin.readline().strip())
sys.stdout.write(str(res))