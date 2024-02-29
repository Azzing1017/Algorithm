def solution(progresses, speeds):
    answer = []
    tmp = []
    answer = [1]
    tmp.append(-((-(100-progresses[0]))//speeds[0]))
    for i in range(1, len(progresses)):
        day = -((progresses[i]-100)//speeds[i])
        if tmp[-1] >= day:
            answer[-1] += 1
        else:
            tmp.append(day)
            answer.append(1)
        
    return answer