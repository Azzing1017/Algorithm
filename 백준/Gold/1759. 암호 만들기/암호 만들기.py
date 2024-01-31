import sys

L, C = map(int, input().split())
list_input = list(map(str, input().split()))
list_input.sort()
list_gather = ['a', 'e', 'i', 'o', 'u']
# tf = [False]*C
list_select = []

def select(index, start, L, C):
    if index == L:
        tf_gather = False
        count_consonant = 0
        for i in list_select:
            if i in list_gather:
                tf_gather = True
            else:
                count_consonant += 1
        if tf_gather and count_consonant>=2:
            sys.stdout.write(''.join(map(str, list_select))+'\n')
        return
    else:
        for i in range(start, C):
            list_select.append(list_input[i])
            select(index+1, i+1, L, C)
            list_select.pop()

select(0, 0, L, C)