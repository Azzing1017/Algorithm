import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li=[[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    li[x].append(y)
    li[y].append(x)

que = []
li_temp = [False] * N

check = False
def go(index, i, N, M):
    global check
    if index == 5:
        check = True
        return
    else:
        for j in li[i]:
            if li_temp[j]:
                continue
            else:
                que.append(j)
                li_temp[j] = True
                go(index+1, j, N, M)
                que.pop()
                li_temp[j] = False

for i in range(N):
    que.append(i)
    li_temp[i] = True
    go(1, i, N, M)
    que.pop()
    li_temp[i] = False
    if check:
        sys.stdout.write('1')
        break

if not check:
    sys.stdout.write('0')