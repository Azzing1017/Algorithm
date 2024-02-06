n = int(input())
li = [0, 1, 3]
for i in range(3, n+1):
    li.append((li[i-1]+li[i-2]+li[i-2])%10007)

print(li[n])