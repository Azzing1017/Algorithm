N = int(input())
list_input = [list(map(int, input().split())) for _ in range(N)]
list_start = [0] * N
gap_sum_min = 10000

def gogo(index, start, N):
    global list_input, list_start, list_link, gap_sum_min
    if N-start < N/2-index:
        return 
    elif index == N/2:
        sum_start=0
        sum_link=0
        for a in range(N):
            for b in range(N):
                if (list_start[a]==list_start[b]==0) and (a!=b):
                    sum_start += list_input[a][b]
                elif (list_start[a]==list_start[b]==1) and (a!=b):
                    sum_link += list_input[a][b]
        gap_sum = abs(sum_start-sum_link)
        if gap_sum_min > gap_sum:
            gap_sum_min = gap_sum
        return
    else:
        for i in range(start, N):
            list_start[i] = 1
            gogo(index+1, i+1, N)
            list_start[i] = 0

gogo(0, 0, N)
print(gap_sum_min)