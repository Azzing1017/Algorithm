from collections import deque

def solution(n, edge):
    answer = 0
    graph = {i:[] for i in range(1, n+1)}
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    que = deque([])
    distance = [0] * (n + 1)
    distance[1] = 1
    que.append(1)
    
    while que:
        x = que.popleft()
        for i in graph[x]:
            if distance[i] == 0:
                distance[i] = distance[x] + 1
                que.append(i)
                
    answer = distance.count(max(distance))
    
    return answer