import sys

N = int(input())
M = int(input())
btn_list = [True]*10
if M != 0:
    btn_nlist = list(map(int, input().split()))
    for i in btn_nlist:
        btn_list[i] = False

count = abs(N-100)
N_up = N
N_down = N
while N_down >= 0 and N_up <= 1000000:
    N_uplist = list(map(int, list(str(N_up))))
    N_downlist = list(map(int, list(str(N_down))))
    N_upcheck = True
    N_downcheck = True
    if N_down >= 0:
        for b in N_downlist:
            if not btn_list[b]:
                N_downcheck = False
                break
        if N_downcheck:
            count_down = len(N_downlist) + N - N_down
            if count >= count_down:
                count = count_down
            break
    if N_up <= 1000000:
        for a in N_uplist:
            if not btn_list[a]:
                N_upcheck = False
                break
        if N_upcheck:
            count_up = len(N_uplist) + N_up - N
            if count >= count_up:
                count = count_up
            break
    N_up += 1
    if N_down > 0:
        N_down -= 1

print(count)