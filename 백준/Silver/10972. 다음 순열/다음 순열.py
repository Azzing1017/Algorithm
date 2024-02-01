N = int(input())
list_input = list(map(int, input().split()))

num = 0
for i in range(-1, -N-1, -1):
    if i == -N:
        num=0
    else:
        if list_input[i] < list_input[i-1]:
            continue
        elif list_input[i] > list_input[i-1]:
            num = i-1
            break

if num == 0:
    print(-1)
else:
    list_a = list_input[:num]
    list_b = list_input[num:num+1]
    list_c = list_input[num+1:]
    list_c_temp = list_input[num+1:]
    list_answer = []

    n=-1
    while True:
        if list_b[0] < list_c[n]:      
            list_c[n] = list_b[0]
            list_b[0] = list_c_temp[n]
            list_c.sort()
            list_answer = list_a + list_b + list_c
            break
        else:
            n -= 1
    
    print(' '.join(map(str, list_answer)))