N = int(input())
li = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]
# 빨강0 초록1 파랑2
li_ans = [[0, 0, 0] for _ in range(N+1)]
for i in range(1, N+1):
    li_ans[i][0] = min(li_ans[i-1][1], li_ans[i-1][2]) + li[i][0]
    li_ans[i][1] = min(li_ans[i-1][0], li_ans[i-1][2]) + li[i][1]
    li_ans[i][2] = min(li_ans[i-1][0], li_ans[i-1][1]) + li[i][2]

li_ans[N].sort()
print(li_ans[N][0])