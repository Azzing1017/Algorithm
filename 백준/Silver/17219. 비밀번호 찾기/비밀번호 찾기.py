N, M = map(int, input().split())
dic = {}
for _ in range(N):
    pg, pw = map(str, input().split())
    dic[pg] = pw

for _ in range(M):
    print(dic[input()])