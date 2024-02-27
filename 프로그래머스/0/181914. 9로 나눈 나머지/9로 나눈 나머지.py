def solution(number):
    answer = 0
    x = int(number) % 9
    y = sum(map(int, list(number))) % 9
    if x == y:
        answer = x
    else:
        answer = 'False'
    return answer