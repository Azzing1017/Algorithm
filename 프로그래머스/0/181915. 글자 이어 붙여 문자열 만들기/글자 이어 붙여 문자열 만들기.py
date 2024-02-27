from collections import deque

def solution(my_string, index_list):
    answer = ''
    index_list = deque(index_list)
    while index_list:
        i = index_list.popleft()
        answer += my_string[i]
    return answer