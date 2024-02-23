import heapq


def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    
    cnt = 0
    while True:
        x = heapq.heappop(scoville)
        if x >= K:
            return cnt
        if len(scoville) == 0:
            return -1
        y = heapq.heappop(scoville)
        z = x + (y * 2)
        cnt += 1
        heapq.heappush(scoville, z)
