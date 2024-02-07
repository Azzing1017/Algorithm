N = int(input())
li = list(map(int, input().split()))
li_ans = [[0,0] for _ in range(N)]

for i in range(0, N):
    for j in range(i):
        if li[i] > li[j]:
            li_ans[i][0] = max(li_ans[i][0], li_ans[j][0] + 1)
    if li_ans[i][0] == 0:
        li_ans[i][0] = 1

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if li[i] > li[j]:
            li_ans[i][1] = max(li_ans[i][1], li_ans[j][1] + 1)
    if li_ans[i][1] == 0:
        li_ans[i][1] = 1

li_ans.sort(key=lambda x:sum(x))
print(sum(li_ans[N-1])-1)
