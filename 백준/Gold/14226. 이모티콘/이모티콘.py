from collections import deque

S = int(input())
li = [0]*1001

for x in range(1, 1001):
    if x<1000:
        if li[x+1] != 0:
            if li[x] > li[x+1] + 1:
                li[x] = li[x+1] + 1
    for i in range(2, 1000//x+1):
        for j in range(x):
            if  not li[x*i-j] or li[x*i-j] > li[x] + i + j:
                li[x*i-j] = li[x] + i + j

print(li[S])