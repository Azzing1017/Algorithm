from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

T = int(input())
for _ in range(T):
    I = int(input())
    tf = [[False]*I for _ in range(I)]
    que = deque([])
    que.append(list(map(int, input().split()))+[0])
    tf[que[0][0]][que[0][1]] = True
    goal = list(map(int, input().split()))
    ans = 0
    while que:
        x, y, cnt = que.popleft()
        if x == goal[0] and y == goal[1]:
            ans = cnt
            break
        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<= nx < I and 0<= ny < I:
                if tf[nx][ny]:
                    continue
                else:
                    que.append([nx, ny, cnt+1])
                    tf[nx][ny] = True
    
    print(ans)
