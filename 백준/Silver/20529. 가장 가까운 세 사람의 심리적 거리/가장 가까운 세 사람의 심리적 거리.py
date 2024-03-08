import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    arr = list(map(str, sys.stdin.readline().split()))
    if N > 32:
        sys.stdout.write(str(0)+'\n')
    else:
        ans = []
        for a in range(N):
            for b in range(a+1, N):
                for c in range(b+1, N):
                    cnt = 0
                    for idx in range(4):
                        if arr[a][idx] != arr[b][idx]:
                            cnt += 1
                        if arr[b][idx] != arr[c][idx]:
                            cnt += 1
                        if arr[c][idx] != arr[a][idx]:
                            cnt += 1
                    ans.append(cnt)
        sys.stdout.write(str(min(ans))+'\n')
