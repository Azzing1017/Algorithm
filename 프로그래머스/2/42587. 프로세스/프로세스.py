from collections import deque

def solution(priorities, location):
    answer = 0
    remain_max = max(priorities)
    priorities = deque(priorities)
    list_length = len(priorities)
    list_location = deque([n for n in range(list_length)])
    cnt = 0
    while priorities:
        if priorities[0] == remain_max:
            cnt += 1
            priorities.popleft()
            if list_location.popleft() == location:
                return cnt
            remain_max = max(priorities)
        else:
            priorities.rotate(-1)
            list_location.rotate(-1)
    
    return answer