N = int(input())
A = list(map(int, input().split()))
D = [[n,1] for n in range(N)]
B = [[n,-1] for n in range(N)]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            if D[i][1] < D[j][1]+1:
                D[i][1] = D[j][1] + 1
                B[i][1] = j

D.sort(key=lambda x:x[1])
print(D[-1][1])
num = D[-1][0]
li_ans = []
while True:
    li_ans.append(A[num])
    num = B[num][1]
    if num == -1:
        break
li_ans.sort()
print(*li_ans)