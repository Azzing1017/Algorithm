N = int(input())
list_input = [list(map(int, input().split())) for _ in range(N)]
list_start = [0] * N
gap_sum_min = 10000

def gogo(index, start, N):
    global list_input, list_start, list_link, gap_sum_min
    sum_start=0
    sum_link=0
    for a in range(N):
        for b in range(N):
            if (list_start[a]==list_start[b]==0) and (a!=b):
                sum_start += list_input[a][b]
    for c in range(N):
        for d in range(N):
            if (list_start[c]==list_start[d]==1) and (c!=d):
                sum_link += list_input[c][d]
    gap_sum = abs(sum_start-sum_link)
    if gap_sum_min > gap_sum:
        gap_sum_min = gap_sum
                
    for i in range(start, N):
        list_start[i] = 1
        gogo(index+1, i+1, N)
        list_start[i] = 0

gogo(0, 0, N)
print(gap_sum_min)