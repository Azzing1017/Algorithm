from collections import deque

def solution(k, dungeons):
    global answer
    answer = -1
    for i in range(len(dungeons)):
        dungeons[i].append(dungeons[i][0] - dungeons[i][1])
    dungeons.sort(key=lambda x: (-x[2], -x[0]))
    
    def go(idx, cur, cnt):
        global answer
        if answer < cnt:
            answer = cnt
        for i in range(idx, len(dungeons)):
            m, n, k = dungeons[i]
            if cur >= m:
                go(i+1, cur-n, cnt+1)
    
    go(0, k, 0)

    return answer
