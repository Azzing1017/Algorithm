from collections import deque
import heapq

def solution(operations):
    answer = []
    
    operations = deque(operations)
    hpq = []
    heapq.heapify(hpq)
    
    while operations:
        x, y = map(str, operations.popleft().split())
        if x == 'I':
            heapq.heappush(hpq, int(y))
        elif hpq and x == 'D':
            if y == '1':
                hpq.remove(max(hpq))
            elif y == '-1':
                heapq.heappop(hpq)
    if hpq:
        answer = [max(hpq), min(hpq)]
    else:
        answer = [0, 0]
    
    return answer