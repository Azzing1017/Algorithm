import sys

N = int(input())
li = [int(input()) for _ in range(N)]

li_temp = []
li_ans = []

num = 1

def sol():
    global li, li_temp, li_ans, num
    for val in li:
        while num <= val:
            li_temp.append(num)
            li_ans.append('+')
            num += 1
        if li_temp.pop() != val:
            return 'NO'
        else:
            li_ans.append('-')
    return '\n'.join(map(str, li_ans))

sys.stdout.write(sol())