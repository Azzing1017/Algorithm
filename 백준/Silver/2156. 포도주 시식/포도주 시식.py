n = int(input())
li = [0] + [int(input()) for _ in range(n)]
li_ans = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    li_ans[i][0] = max(li_ans[i-1][0], li_ans[i-1][1], li_ans[i-1][2])
    li_ans[i][1] = li_ans[i-1][0] + li[i]
    li_ans[i][2] = li_ans[i-1][1] + li[i]

li_ans[n].sort()
print(li_ans[n].pop())