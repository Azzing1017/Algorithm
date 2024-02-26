def solution(brown, yellow):
    answer = []
    for x in range(yellow, 0, -1):
        if yellow%x == 0:
            y = yellow//x
            if 2*x + 2*y + 4 == brown:
                answer = [x+2, y+2]
                return answer