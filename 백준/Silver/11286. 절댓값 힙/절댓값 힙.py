import sys
import heapq


N = int(sys.stdin.readline().strip())
arr = [int(read_line.strip()) for read_line in sys.stdin.readlines()]


hpq = []
heapq.heapify(hpq)
ans = []
for x in arr:
    if x != 0:
        heapq.heappush(hpq,(abs(x), x))
    else:
        try:
            ans.append(heapq.heappop(hpq)[1])
        except IndexError:
            ans.append(0)


sys.stdout.write('\n'.join(map(str, ans)))
