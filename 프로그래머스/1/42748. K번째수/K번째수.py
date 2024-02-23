from collections import deque

def solution(array, commands):
    answer = []
    commands = deque(commands)
    while commands:
        i, j, k = commands.popleft()
        li = array[i-1:j]
        li.sort()
        answer.append(li[k-1])
    return answer