def solution(array):
    answer = 0
    dic = {}
    # 각 요소의 등장 횟수를 세기
    for i in array:
        dic[i] = dic.get(i, 0) + 1

    # 딕셔너리를 값에 따라 내림차순으로 정렬
    sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    
    tmp_k = -1
    tmp_v = -1
    for k, v in sorted_dic.items():
        if tmp_k == -1:
            tmp_k = k
            tmp_v = v
        else:
            if tmp_v == v:
                return -1
            else:
                return tmp_k
    if tmp_k != -1:
        return tmp_k