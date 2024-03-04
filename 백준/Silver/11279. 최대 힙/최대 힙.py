import sys
import heapq

read_lines = sys.stdin.readlines()

arr = []
heapq.heapify(arr)

ans = []
for read_line in read_lines[1:]:
    x = int(read_line.strip())
    if x != 0:
        heapq.heappush(arr, -x)
    else:
        try:
            ans.append(-heapq.heappop(arr))
        except IndexError:
            ans.append(0)

sys.stdout.write('\n'.join(map(str, ans)))
