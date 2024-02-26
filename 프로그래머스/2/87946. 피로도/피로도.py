from collections import deque

def solution(k, dungeons):
    global max_num
    answer = -1
    max_num = 0
    
    def go(cur, cnt):
        global max_num
        for i, v in enumerate(dungeons):
            m, n = v
            if tf[i] == False and cur >= m:
                tf[i] = True
                if max_num < cnt+1:
                    max_num = cnt+1
                go(cur - n, cnt + 1)
                tf[i] = False
    
    tf = [False] * len(dungeons)
    go(k, 0)
    answer = max_num
    
    return answer
