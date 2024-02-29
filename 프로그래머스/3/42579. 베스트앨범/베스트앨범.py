from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dic1 = defaultdict(int)
    dic2 = defaultdict(list)
    for i, val in enumerate(zip(genres, plays)):
        k, v = val
        dic1[k] += v
        dic2[k].append([v, i])
    dic1 = dict(sorted(dic1.items(), key=lambda x: -x[1]))
    
    for k in dic1.keys():
        dic2[k].sort(key=lambda x: -x[0])
        for a, idx in dic2[k][:2]:
            answer.append(idx)
    
    return answer
