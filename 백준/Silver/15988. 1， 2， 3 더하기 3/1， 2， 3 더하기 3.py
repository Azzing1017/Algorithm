import sys

limit = 1000000
mod = 1000000009

li = [0] * (limit+1)
li[1] = 1
li[2] = 2
li[3] = 4
for i in range(4, limit+1):
    li[i] = (li[i] + li[i-1])%mod
    li[i] = (li[i] + li[i-2])%mod
    li[i] = (li[i] + li[i-3])%mod
    li[i] %= mod

T = int(sys.stdin.readline())
for _ in range(T):
    sys.stdout.write(str(li[int(sys.stdin.readline())])+'\n')