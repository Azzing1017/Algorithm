N, S = map(int, input().split())
list_input = list(map(int, input().split()))
list_tf = [False]*N

list_select = []
count = 0

def go(start, N, S):
    global list_input, list_tf, count, list_select
    if list_select and sum(list_select) == S:
        count += 1
    for i in range(start, N):
        if list_tf[i]:
            continue
        else:
            list_select.append(list_input[i])
            list_tf[i] = True
            go(i+1, N, S)
            list_select.pop()
            list_tf[i] = False
            
go(0, N, S)
print(count)