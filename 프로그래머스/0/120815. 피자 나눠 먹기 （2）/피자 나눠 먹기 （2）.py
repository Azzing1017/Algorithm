def solution(n):
    answer = 0
    def go(m, n):
        if n == 0:
            return m
        else:
            return go(n, m%n)
    answer = n // go(max(n, 6), min(n, 6))
    return answer