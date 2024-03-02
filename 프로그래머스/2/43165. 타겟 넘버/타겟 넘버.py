from collections import deque

def solution(numbers, target):
    l = len(numbers)
    que = deque([])
    answer = 0
    cnt = 0
    que.append([0, -numbers[0]])
    que.append([0, numbers[0]])
    while que:
        index, cur = que.popleft()
        index += 1
        if index == l:
            if cur == target:
                cnt += 1
        else:
            que.append([index, cur - numbers[index]])
            que.append([index, cur + numbers[index]])
    answer = cnt
    
    return answer