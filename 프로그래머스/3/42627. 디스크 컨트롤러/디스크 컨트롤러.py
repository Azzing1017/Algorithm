from collections import deque
import heapq
    
def solution(jobs):
    
    jobs.sort(key=lambda x:x[0])
    jobs_length = len(jobs)
    jobs = deque(jobs)
    now_time = 0
    sum_time = 0
    hpq = []
    heapq.heapify(hpq)
    
    while jobs or hpq:
        while jobs:
            if jobs[0][0] <= now_time:
                req_t, dur_t = jobs.popleft()
                heapq.heappush(hpq, [dur_t, req_t])
            else:
                break
        if hpq:
            dur_t, req_t = heapq.heappop(hpq)
            sum_time = sum_time + now_time + dur_t - req_t
            now_time = now_time + dur_t
        else:
            now_time += 1
    
    return sum_time // jobs_length