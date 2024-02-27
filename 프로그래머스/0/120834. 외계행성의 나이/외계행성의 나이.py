def solution(age):
    answer = ''
    li = ['a','b','c','d','e','f','g','h','i','j']
    age = list(str(age))
    for i, v in enumerate(age):
        age[i] = li[int(v)]
    answer = ''.join(map(str, age))
    return answer