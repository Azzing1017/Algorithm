import heapq


def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    
    cnt = 0
    while scoville:
        x = heapq.heappop(scoville)
        if x >= K:
            return cnt
        try:
            y = heapq.heappop(scoville)
            z = x + (y * 2)
            cnt += 1
            heapq.heappush(scoville, z)
        except IndexError:
            return -1
