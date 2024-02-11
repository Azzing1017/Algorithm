N = int(input())
li = list(map(int, input().split()))
li.sort()

sum = 0
for i in range(N):
    sum += li[i]*(N-i)

print(sum)