from collections import defaultdict

def solution(tickets):
    answer = []
    
    tickets.sort(key=lambda x: x[1])
    l = len(tickets)
    tf = [True] * l
    dic = defaultdict(list)
    for i, ticket in enumerate(tickets):
        dic[ticket[0]].append(i)
    ans = []
    
    def go(port, index, tmp, l):
        if index == l+1:
            ans.append(tmp)
        else:
            for i in dic[port]:
                if tf[i]:
                    tf[i] = False
                    go(tickets[i][1], index+1, tmp + [tickets[i][1]], l)
                    tf[i] = True
    go("ICN", 1, ["ICN"], l)
    answer = ans[0]
    return answer