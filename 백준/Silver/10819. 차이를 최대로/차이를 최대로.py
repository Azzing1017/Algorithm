N = int(input())
list_input = list(map(int, input().split()))
list_input.sort()
list_tf = [False] * N
list_answer = []

def cal(N):
    global list_answer
    sum = 0
    for i in range(N-1):
        sum = sum + abs(list_answer[i] - list_answer[i+1])
    return sum

max = 0
def go(index, N):
    global list_answer, max
    if index == N:
        sum_cal = cal(N)
        if max < sum_cal:
            max = sum_cal
        return
    else:
        for i in range(N):
            if list_tf[i]:
                continue
            else:
                list_answer.append(list_input[i])
                list_tf[i] = True
                go(index+1, N)
                list_answer.pop()
                list_tf[i] = False

go(0, N)
print(max)