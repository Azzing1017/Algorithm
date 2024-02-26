def solution(answers):
    answer = []
    p = [[1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, c in enumerate(p):
            if a == c[q%len(c)]:
                s[i] += 1
    max_cor = max(s)
    answer = [i for i, cor in enumerate(s, start = 1) if cor == max_cor]
    
    return answer