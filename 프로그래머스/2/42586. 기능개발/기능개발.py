from collections import deque

def solution(progresses, speeds):
    answer = []
    ll = len(progresses)
    tmp = deque([])
    for i in range(ll):
        remain_day = (100 - progresses[i])//speeds[i]
        if (100 - progresses[i])%speeds[i] != 0:
            remain_day += 1
        tmp.append(remain_day)
    if ll == 1:
        answer = [1]
    else:
        t = tmp.popleft()
        cnt = 1
        for _ in range(ll-1):
            x = tmp.popleft()
            if t >= x:
                cnt += 1
            else:
                answer.append(cnt)
                t = x
                cnt = 1
        answer.append(cnt)
        
    return answer