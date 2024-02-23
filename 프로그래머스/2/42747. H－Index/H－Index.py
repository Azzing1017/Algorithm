def solution(citations):
    answer = 0
    list_length = len(citations)
    citations.sort(reverse = True)
    h = 0
    for i in range(list_length):
        h = i + 1
        if citations[i] >= h:
            continue
        else:
            return h - 1
    return list_length