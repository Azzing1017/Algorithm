def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    while completion:
        n = participant.pop()
        m = completion.pop()
        if n == m:
            continue
        else:
            answer = n
            break
    if not answer:
        answer = participant[0]
    return answer