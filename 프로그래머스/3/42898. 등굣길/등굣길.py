def solution(m, n, puddles):
    answer = 0
    MOD = 1000000007
    arr = [[-1]*m for _ in range(n)]
    for y, x in puddles:
        arr[x-1][y-1] = 0
    arr[0][0] = 1
    for x in range(n):
        for y in range(m):
            if arr[x][y] == -1:
                a = 0
                b = 0
                if x!=0:
                    a = arr[x-1][y]
                if y!=0:
                    b = arr[x][y-1]
                arr[x][y] = (a+b)%MOD
    answer = (arr[n-1][m-1])%MOD
    return answer