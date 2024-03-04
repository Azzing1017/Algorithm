N, K = map(int, input().split())
li = []
for _ in range(N):
    a = int(input())
    if a <= K:
        li.append(a)
    else:
        break
cnt = 0
while K != 0:
    x = li.pop()
    cnt += K//x
    K = K%x
print(cnt)
