def solution(n, computers):
    answer = 0
    
    tf = [0] * n
    
    def dfs(x):
        tf[x] = 1
        for a in range(n):
            if not tf[a]:
                if computers[x][a] == 1:
                    dfs(a)
    
    for i in range(n):
        if tf[i]:
            continue
        else:
            answer += 1
            dfs(i)
    
    return answer