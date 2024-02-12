import sys
import heapq


N = int(sys.stdin.readline().strip())


que = []
heapq.heapify(que)
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if que:
            sys.stdout.write(str(heapq.heappop(que))+'\n')
        else:
            sys.stdout.write('0'+'\n')
    else:
        heapq.heappush(que, x)