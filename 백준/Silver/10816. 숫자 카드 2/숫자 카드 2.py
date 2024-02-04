N = int(input())
li_N = list(map(int, input().split()))
M = int(input())
li_M = list(map(int, input().split()))

dic_N ={}
for _ in range(N):
    if li_N[-1] in dic_N.keys():
        dic_N[li_N.pop()] += 1
    else:
        dic_N[li_N.pop()] = 1

for i in li_M:
    if i in dic_N.keys():
        print(dic_N[i], end =" ")
    else:
        print(0, end=" ")