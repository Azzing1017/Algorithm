def solution(l, r):
    answer = []
    i = 1
    n = 5

    while True:
        if n > r: break
        n = 5 * int(bin(i)[2:])
        if l <= n <= r:
            answer.append(n)
        i += 1

    return [-1] if len(answer) == 0 else answer