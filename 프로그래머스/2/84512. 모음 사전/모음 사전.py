def solution(word):
    answer = 0
    li = ['','A','E','I','O','U']
    ans = []
    for a in li:
        for b in li:
            for c in li:
                for d in li:
                    for e in li:
                        tmp = ''
                        tmp = a+b+c+d+e
                        ans.append(tmp)
    ans = set(ans)
    ans = sorted(ans, key=lambda x: x)
    answer = ans.index(word)
    return answer