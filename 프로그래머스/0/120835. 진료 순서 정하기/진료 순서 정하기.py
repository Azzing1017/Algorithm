def solution(emergency):
    answer = []
    li = []
    for i, v in enumerate(emergency):
        li.append([i, v])
    li.sort(key=lambda x: x[1])
    l = len(emergency)
    answer = [0] * l
    for i, v in enumerate(li):
        answer[v[0]] = l - i
    return answer