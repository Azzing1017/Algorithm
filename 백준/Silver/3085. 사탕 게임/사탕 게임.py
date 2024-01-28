import sys
N = int(input())
candy_list = [list(map(str, list(input()))) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


a_count = 0
a_countmax = 1
for i in range(N):
    a = ""
    for j in range(N):
        if a != candy_list[i][j]:
            a = candy_list[i][j]
            a_count = 1
        else:
            a_count += 1
            if a_countmax < a_count:
                a_countmax = a_count
for j in range(N):
    a = ""
    for i in range(N):
        if a != candy_list[i][j]:
            a = candy_list[i][j]
            a_count = 1
        else:
            a_count += 1
            if a_countmax < a_count:
                a_countmax = a_count

def max_length(x, y):
    global candy_list
    b = ""
    b_count = 0
    b_countmax = 1
    for i in range(N):
        if b != candy_list[i][y]:
            b = candy_list[i][y]
            b_count = 1
        else:
            b_count += 1
            if b_countmax < b_count:
                b_countmax = b_count
    b = ""
    for i in range(N):
        if b != candy_list[x][i]:
            b = candy_list[x][i]
            b_count = 1
        else:
            b_count += 1
            if b_countmax < b_count:
                b_countmax = b_count    
    return b_countmax

max = 0
for i in range(N):
    for j in range(N):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
                
            if 0<=nx<N and 0<=ny<N:
                temp1 = candy_list[i][j]
                temp2 = candy_list[i + dx[k]][j + dy[k]]
                candy_list[i][j] = temp2
                candy_list[i + dx[k]][j + dy[k]] = temp1
                find_max = max_length(nx, ny)
                if max < find_max:
                    max = find_max
                candy_list[i][j] = temp1
                candy_list[i + dx[k]][j + dy[k]] = temp2

print(max)