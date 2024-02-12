N, M, R = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
cal = list(map(int, input().split()))

def cal1():
    global li, N, M
    li_cal = [[0]*M for _ in range(N)]
    for i in range(N):
        li_cal[i] = li[N-1-i]
    li = li_cal

def cal2():
    global li, N, M
    li_cal = [[0]*M for _ in range(N)]
    for j in range(M):
        for i in range(N):
            li_cal[i][j] = li[i][M-1-j]
    li = li_cal

def cal3():
    global li, N, M
    N, M = M, N
    li_cal = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            li_cal[i][j] = li[M-1-j][i]
    li = li_cal

def cal4():
    global li, N, M
    N, M = M, N
    li_cal = [[0]*M for _ in range(N)]
    for i in range(N):
            for j in range(M):
                li_cal[i][j] = li[j][N-1-i]
    li = li_cal
    
def cal5():
    global li, N, M
    li_1 = li[0:N//2]
    li_4 = li[N//2:N]
    li_2 = [[0] * (M//2) for _ in range(N//2)]
    li_3 = [[0] * (M//2) for _ in range(N//2)]
    for i in range(N//2):
        li_2[i] = li_1[i][M//2:M]
        li_1[i] = li_1[i][0:M//2]
        li_3[i] = li_4[i][M//2:M]
        li_4[i] = li_4[i][0:M//2]
        li_4[i] = li_4[i]+li_1[i]
        li_3[i] = li_3[i]+li_2[i]
    li = li_4+li_3

def cal6():
    global li, N, M
    li_1 = li[0:N//2]
    li_4 = li[N//2:N]
    li_2 = [[0] * (M//2) for _ in range(N//2)]
    li_3 = [[0] * (M//2) for _ in range(N//2)]
    for i in range(N//2):
        li_2[i] = li_1[i][M//2:M]
        li_1[i] = li_1[i][0:M//2]
        li_3[i] = li_4[i][M//2:M]
        li_4[i] = li_4[i][0:M//2]
        li_2[i] = li_2[i]+li_3[i]
        li_1[i] = li_1[i]+li_4[i]
    li = li_2+li_1

for i in range(R):
    x = cal[i]
    if x == 1:
        cal1()
    elif x == 2:
        cal2()
    elif x == 3:
        cal3()
    elif x == 4:
        cal4()
    elif x == 5:
        cal5()
    elif x == 6:
        cal6()
    else:
        break
        
for i in li:
    print(*i)