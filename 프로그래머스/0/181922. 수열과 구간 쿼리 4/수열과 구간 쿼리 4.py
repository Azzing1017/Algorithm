def solution(arr, queries):
    answer = []
    for val in queries:
        s, e, k = val[0], val[1], val[2]
        for i in range(s, e+1):
            if i == 0:
                arr[0] += 1
            elif i%k == 0:
                arr[i] += 1
    answer = arr
    return answer