from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for v, k in clothes:
        dic[k] += 1
    for v in dic.values():
        answer *= (v + 1)
    answer -= 1
    return answer