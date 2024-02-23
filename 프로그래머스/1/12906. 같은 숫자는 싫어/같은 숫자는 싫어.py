from collections import deque

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    arr = deque(arr)
    answer.append(arr.popleft())
    
    list_length = len(arr)
    for _ in range(list_length):
        x = arr.popleft()
        if answer[-1] == x:
            continue
        else:
            answer.append(x)
        
    return answer