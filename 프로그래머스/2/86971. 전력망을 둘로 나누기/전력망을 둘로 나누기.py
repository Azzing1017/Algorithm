def solution(n, wires):
    global cnt
    answer = n
    li = [[] for _ in range(n+1)]
    for x, y in wires:
        li[x].append(y)
        li[y].append(x)
    
    def go(x):
        global cnt
        tf[x] = True
        cnt += 1
        for i in li[x]:
            if tf[i] == False:
                go(i)
    
    for x, y in wires:
        cnt = 0
        tf = [False] * (n+1)
        li[x].remove(y)
        li[y].remove(x)
        go(1)
        if answer > abs(n-2*cnt):
            answer = abs(n-2*cnt)
        li[x].append(y)
        li[y].append(x)
    
    return answer