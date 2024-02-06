N = int(input())
li = [n for n in range(N+1)]

for i in range(1, N+1):
    for j in range(1, int(i**(1/2))+1):
        li[i] = min(li[i], li[i-j**2]+1)

print(li.pop())