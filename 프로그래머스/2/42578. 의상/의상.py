def solution(clothes):
    answer = 1
    dic = {}
    for var in clothes:
        x = var[1]
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    for val in dic.values():
        answer *= (val + 1)
    answer -= 1
    return answer