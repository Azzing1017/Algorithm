def solution(genres, plays):
    answer = []
    list_length = len(genres)
    dic = {}
    for i in range(list_length):
        if genres[i] in dic:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]][1].append([plays[i], i])
        else:
            dic[genres[i]] = [plays[i], [[plays[i], i]]]
    dic = dict(sorted(dic.items(), key=lambda x:-x[1][0]))
    for v in dic.values():
        v[1].sort(key=lambda x:-x[0])
        cnt = 0
        for val in v[1]:
            answer.append(val[1])
            cnt += 1
            if cnt == 2:
                break
    return answer