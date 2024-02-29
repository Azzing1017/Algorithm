from collections import deque

def solution(n, results):
    answer = 0
    
    arr = [[0]*n for _ in range(n)]
    for x, y in results:
        arr[x-1][y-1] = 1
        arr[y-1][x-1] = -1
    for a in range(n):
        for b in range(n):
            if arr[a][b] != 0:
                wl = arr[a][b]
                que = deque([])
                que.append(b)
                while que:
                    x = que.popleft()
                    for i in range(n):
                        if i != a and arr[x][i] == wl and arr[a][i] == 0:
                            arr[a][i] = wl
                            arr[i][a] = -wl
                            que.append(i)
                            
    cnt = 0
    for v in arr:
        if v.count(0) == 1:
            cnt += 1
    answer = cnt
                
    return answer