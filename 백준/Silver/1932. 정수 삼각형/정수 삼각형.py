n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li_ans = [[0]*(i+2) for i in range(1, n+1)]
li_ans[0][1] = li[0][0]

for i in range(1, n):
    for j in range(1, i+2):
        li_ans[i][j] = max(li_ans[i-1][j-1], li_ans[i-1][j]) + li[i][j-1]

print(max(li_ans[n-1]))