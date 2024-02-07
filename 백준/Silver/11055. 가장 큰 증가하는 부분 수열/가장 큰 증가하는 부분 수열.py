A = int(input())
li = list(map(int, input().split()))

li_ans = [0] * A
li_ans[0] = li[0]

for i in range(1, A):
    for j in range(0, i):
        if li[i] > li[j]:
            li_ans[i] = max(li_ans[i], li_ans[j] + li[i])
    if li_ans[i] == 0:
        li_ans[i] = li[i]

print(max(li_ans))