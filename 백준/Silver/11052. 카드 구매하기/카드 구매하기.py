N = int(input())
li = list(map(int, [0]+input().split()))
li_ans = [0, li[1]]

for i in range(2, N+1):
    li_temp = []
    li_temp.append(li[i])
    for j in range(1, i//2+1):
        li_temp.append(li_ans[i-j]+li_ans[j])
    li_temp.sort()
    li_ans.append(li_temp.pop())

print(li_ans.pop())