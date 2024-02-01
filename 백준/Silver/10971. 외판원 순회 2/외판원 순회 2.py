N = int(input())
list_input = [list(map(int, input().split())) for _ in range(N)]

list_num = [n for n in range(N)]
list_tf = [False]*N

list_select = []

def cal(N):
    sum = 0
    for i in range(-1, N-1):
        sum_check = list_input[list_num[list_select[i]]][list_num[list_select[i+1]]]
        if sum_check != 0:
            sum += sum_check
        else:
            sum = 0
            return sum
    return sum

sum_min = 10000000
def go(index, N):
    global sum_min, list_select, list_num, list_tf
    if index == N:
        sum_check = cal(N)
        if sum_check == 0:
            return
        elif sum_min > sum_check:
            sum_min = sum_check
        return
    else:
        for i in range(N):
            if list_tf[i]:
                    continue
            else:
                list_select.append(list_num[i])
                list_tf[i] = True
                go(index+1, N)
                list_select.pop()
                list_tf[i] = False

go(0, N)
print(sum_min)