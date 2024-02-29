def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse = True)
    for i, h in enumerate(citations):
        if i+1 > h:
            return i
    return n