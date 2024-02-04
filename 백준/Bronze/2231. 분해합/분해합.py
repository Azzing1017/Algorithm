N = int(input())

check = -1
for i in range(N):
    li = list(map(int, list(str(i))))
    M = i + sum(li)
    if M == N:
        check = i
        break

if check != -1:
    print(check)
else:
    print(0)