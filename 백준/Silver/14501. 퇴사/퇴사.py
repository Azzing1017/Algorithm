N = int(input())
list_input = [list(map(int, input().split())) for _ in range(N)]
tf = [False] * N
list_select_day = []
list_select_pay = []
max_sum = 0

def max_revenue(start, N):
    global list_input, max_sum, list_select
    for i in range(start, N):
        list_select_day.append(list_input[i][0])
        list_select_pay.append(list_input[i][1])
        sum_list_select = sum(list_select_pay)
        if i + list_select_day[-1] == N:
            if max_sum < sum_list_select:
                max_sum = sum_list_select
        elif i + list_select_day[-1] > N:
            if max_sum < sum_list_select - list_select_pay[-1]:
                max_sum = sum_list_select - list_select_pay[-1]
        else:
            max_revenue(i+list_select_day[-1], N)
        list_select_day.pop()
        list_select_pay.pop()

max_revenue(0, N)
print(max_sum)