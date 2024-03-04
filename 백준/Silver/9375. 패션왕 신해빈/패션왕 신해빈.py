from collections import defaultdict

for _ in range(int(input())):
    dic = defaultdict(int)
    for _ in range(int(input())):
        v, k = map(str, input().split())
        dic[k] += 1
    cnt = 1
    for v in dic.values():
        cnt *= (v+1)
    print(cnt-1)
    