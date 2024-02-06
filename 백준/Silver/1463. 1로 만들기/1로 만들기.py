N = int(input())

li = [0, 0, 1, 1]
num = 4
while num < N+1:
    li_temp = []
    if num % 3 == 0:
        li_temp.append(li[num//3]+1)
    if num % 2 == 0:
        li_temp.append(li[num//2]+1)
    li_temp.append(li[num-1]+1)
    li_temp.sort()
    li.append(li_temp[0])
    num += 1

print(li[N])