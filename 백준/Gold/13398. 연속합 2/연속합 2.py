N = int(input())
li = list(map(int, input().split()))
li_ans = [[-100000000, -100000000] for _ in range(N)]
li_ans[0][0] = li[0]

for i in range(1, N):
    li_ans[i][0] = max(li_ans[i-1][0]+li[i], li[i])
    li_ans[i][1] = max(li_ans[i-1][0], li_ans[i-1][1]+li[i])

li_ans.sort(key=lambda x:x[1])
a = li_ans[N-1][1]
li_ans.sort(key=lambda x:x[0])
b = li_ans[N-1][0]
print(max(a, b))