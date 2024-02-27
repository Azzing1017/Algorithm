def solution(n):
    answer = []
    def go(x, answer):
        answer.append(x)
        if x == 1:
            return answer
        else:
            if x%2 == 0:
                return go(x//2, answer)
            else:
                return go(3*x+1, answer)
    answer = go(n, [])
    return answer