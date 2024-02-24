import sys
n = int(input())
factor = list(map(int, input().split()))
factor.sort()
sys.stdout.write(str(factor[0]*factor[-1]))