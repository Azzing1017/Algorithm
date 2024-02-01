import sys

n = int(input())
str_input = str(input())
list_input = [char for char in str_input]

list_sort = [[0]*n for _ in range(n)]
count=0
for i in range(n):
    for j in range(i, n):
        if list_input[count] == '+':
            list_sort[i][j] = 1
        elif list_input[count] == '-':
            list_sort[i][j] = -1
        elif list_input[count] == '0':
            list_sort[i][j] = 0
        count += 1

list_select = []

def gogo(index):
    global list_sort, list_select
    sum_check = 0
    for i in range(index, -1, -1):
        sum_check += list_select[i]
        if list_sort[i][index] == 1:
            if sum_check > 0:
                continue
            else:
                return False
        elif list_sort[i][index] == 0:
            if sum_check == 0:
                continue
            else:
                return False
        elif list_sort[i][index] == -1:
            if sum_check < 0:
                continue
            else:
                return False
    return True

def go(index, n):
    global list_sort, list_select
    if not gogo(index-1):
        return
    if index == n:
        sys.stdout.write(' '.join(map(str, list_select))+'\n')
        sys.exit()
        return
    else:
        if list_sort[index][index] == 1:
            for j in range(1, 11):
                list_select.append(j)
                go(index+1, n)
                list_select.pop()
        elif list_sort[index][index] == 0:
            list_select.append(0)
            go(index+1, n)
            list_select.pop()
        elif list_sort[index][index] == -1:
            for j in range(-10, 0):
                list_select.append(j)
                go(index+1, n)
                list_select.pop()

go(0, n)