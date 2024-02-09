from collections import deque
import sys
sys.setrecursionlimit(21000)

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    li = [[] for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        li[x].append(y)
        li[y].append(x)
    tf = [0] * (V+1)
    que = deque([])

    check = True
    for i in range(1, V+1):
        if check:
            if tf[i] == 0:
                tf[i] = 1
                que.append(i)
                while que:
                    temp = que.popleft()
                    tf_temp = tf[temp]
                    for j in li[temp]:
                        if tf[j] == 0:
                            tf[j] = -tf_temp
                            que.append(j)
                        elif tf[j] == -tf_temp:
                            continue
                        elif tf[j] == tf_temp:
                            check = False
                            break
                    if not check:
                        break 
            else:
                continue
        else:
            break

    if check:
        print('YES')
    else:
        print('NO')