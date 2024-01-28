import sys

list = [0]*1000001
list[1] = 1

for i in range(2, 1001):
    if list[i] == 0:
        per = 2
        while i*per <= 1000000:
            list[i*per] = 1
            per += 1

M, N = map(int, input().split())
answer = []
for k in range(M, N+1):
    if list[k] == 0:
        answer.append(k)

sys.stdout.write('\n'.join(map(str, answer))+'\n')