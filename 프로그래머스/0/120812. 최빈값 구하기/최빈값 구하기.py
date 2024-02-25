def solution(array):
    keys = set(array)
    dict = {}
    max_freq = []
    for key in keys:
        dict[key] = array.count(key)
    for key in keys:
        if dict[key] == max(dict.values()):
            max_freq.append(key)
    if len(max_freq) > 1:
        answer = -1
    else:
        answer = max_freq[0]
    return answer