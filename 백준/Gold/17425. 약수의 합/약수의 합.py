import sys

test_case = 1000000
g_sumlist = [1] * (test_case+1)
N_sumlist = [1] * (test_case+1)

for i in range(2, test_case+1):
    j=1
    while i*j <= test_case:
        g_sumlist[j*i] += i
        j += 1
    N_sumlist[i] = N_sumlist[i-1] + g_sumlist[i]

T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    answer.append(N_sumlist[N])

sys.stdout.write('\n'.join(map(str, answer))+'\n')