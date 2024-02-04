def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)

N = int(input())
num = str(fac(N))
cnt = 0
for i in range(len(num)-1, -1, -1):
    if num[i] == '0':
        cnt += 1
    else:
        break
print(cnt)