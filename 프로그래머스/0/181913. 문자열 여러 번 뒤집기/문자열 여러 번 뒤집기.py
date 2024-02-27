from collections import deque

def solution(my_string, queries):
    answer = ''
    queries = deque(queries)
    while queries:
        x, y = queries.popleft()
        a = my_string[:x]
        b = my_string[x:y+1][::-1]
        c = my_string[y+1:]
        my_string = a + b + c
    answer = my_string
    return answer