def solution(a, b, c, d):
    answer = 0
    li = [a, b, c, d]
    dic = {}
    for i in li:
        dic[i] = dic.get(i, 0) + 1
    length = len(dic)
    dic = dict(sorted(dic.items(), key=lambda x: (-x[1], -x[0])))
    li_dic = list(dic.keys())
    if length == 1:
        answer = a * 1111
    elif length == 2:
        if dic[a] in [1, 3]:
            p = li_dic[0]
            q = li_dic[1]
            answer = (10 * p + q)**2
        else:
            p = li_dic[0]
            q = li_dic[1]
            answer = (p + q) * abs(p - q)
    elif length == 3:
        p = li_dic[0]
        q = li_dic[1]
        r = li_dic[2]
        answer = q * r
    else:
        s = li_dic[3]
        answer = s
    return answer