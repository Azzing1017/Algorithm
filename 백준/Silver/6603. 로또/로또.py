def go(index, start, k, S, list_select):
    if 6 - index > k - start + 1:
        return
    elif index == 6:
        print(' '.join(map(str, list_select)))
        return
    else:
        for i in range(start, k):
            list_select.append(S[i])
            go(index+1, i+1, k, S, list_select)
            list_select.pop()

while True:
    list_input = list(map(int, input().split()))
    k = list_input[0]
    if k == 0:
        break
    else:
        S = list_input[1:]
    list_select = []
    go(0, 0, k, S, list_select)
    print()