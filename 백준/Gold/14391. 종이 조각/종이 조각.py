N, M = map(int, input().split())
list_input = [list(map(str, list(input()))) for _ in range(N)]
list_tf = [[0]*M for _ in range(N)]

list_sum = []

def slc(N, M):
    global list_input, list_tf, list_sum
    sum_all = 0
    for i in range(N):
        str_num = '0'
        for j in range(M):
            if list_tf[i][j] == 0:
                str_num = str_num + list_input[i][j]
            else:
                sum_all += int(str_num)
                str_num = '0'
        sum_all += int(str_num)
    for j in range(M):
        str_num = '0'
        for i in range(N):
            if list_tf[i][j] == 1:
                str_num = str_num + list_input[i][j]
            else:
                sum_all += int(str_num)
                str_num = '0'
        sum_all += int(str_num)
    list_sum.append(sum_all)

def go(index, N, M):
    global list_input, list_select
    if index == N*M:
        slc(N, M)
        return
    for i in range(2):
        if i == 1:
            list_tf[index//M][index%M] = 1
            go(index+1, N, M)
            list_tf[index//M][index%M] = 0
        else:
            go(index+1, N, M)    

go(0, N, M)
list_sum.sort()
print(list_sum[-1])