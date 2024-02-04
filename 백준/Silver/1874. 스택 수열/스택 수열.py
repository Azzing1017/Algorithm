import sys
from collections import deque

N = int(input())
li = [int(input()) for _ in range(N)]
que_li = deque(li)

li_temp = []
li_ans = []

right = -1

num = 1
index = 0

while index < N:
    if que_li:
        left = que_li[0]
    else:
        break
    if num == N+1:
        if li_temp:
            if li_temp.pop() == que_li[0]:
                li_ans.append('-')
                que_li.popleft()
                index += 1
            else:
                break
        else:
            break
    elif num > left:
        if li_temp:
            if li_temp.pop() == left:
                li_ans.append('-')
                que_li.popleft()
                index += 1
            else:
                break
        else:
            break
    elif num == left:
        li_temp.append(num)
        li_ans.append('+')
        num += 1
        que_li.popleft()
        li_temp.pop()
        li_ans.append('-')
        index += 1
    elif num == que_li[right]:
        li_temp.append(num)
        li_ans.append('+')
        num += 1
        right -= 1
    elif num < left:
        li_temp.append(num)
        li_ans.append('+')
        num += 1

if index == N:
    sys.stdout.write('\n'.join(map(str, li_ans))+'\n')
else:
    sys.stdout.write('NO')