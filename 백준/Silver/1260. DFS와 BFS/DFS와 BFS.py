N, M, V = map(int, input().split())
li = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    li[x].append([x, y])
    li[y].append([y, x])
for val in li:
    val.sort(key=lambda x:x[1])

tf = [False]*(N+1)
tf[V] = True
li_tmp = [V]
li_temp = [V]
def dfs():
    global li_temp, li_tmp, tf, li
    if not li_tmp:
        return
    for val in li[li_tmp.pop()]:
        if tf[val[1]]:
            continue
        else:
            li_tmp.append(val[1])
            li_temp.append(val[1])
            tf[val[1]] = True
            dfs()

dfs()
print(*li_temp)

tf = [False]*(N+1)
tf[V] = True
li_tmp = [V]
li_temp = [V]
def bfs():
    global li_temp, li_tmp, tf, li
    if not li_tmp:
        return
    for val in li[li_tmp.pop(0)]:
        if tf[val[1]]:
            continue
        else:
            li_tmp.append(val[1])
            li_temp.append(val[1])
            tf[val[1]] = True
    bfs()

bfs()
print(*li_temp)