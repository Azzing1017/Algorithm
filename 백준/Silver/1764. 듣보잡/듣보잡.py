import sys


N, M = map(int, sys.stdin.readline().split())
dic = {sys.stdin.readline().strip() : 0 for _ in range(N)}


ans = []
for _ in range(M):
    x = sys.stdin.readline().strip()
    try:
        if dic[x] == 0:
            ans.append(x)
    except:
        pass
ans.sort()


sys.stdout.write(str(len(ans)) + '\n' + '\n'.join(map(str, ans)))