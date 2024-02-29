def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    ans = []
    for x, y in routes:
        chk = True
        for z in ans:
            if x <= z <= y:
                chk = False
                break
        if chk:
            ans.append(y)
    answer = len(ans)
    return answer