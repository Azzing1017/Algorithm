def solution(array):
    while len(array) != 0:
        i = -1
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1