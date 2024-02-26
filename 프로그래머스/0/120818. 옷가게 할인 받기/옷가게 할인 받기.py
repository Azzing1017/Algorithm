def solution(price):
    answer = 0
    dic = {500000: 0.8, 300000: 0.9, 100000: 0.95, 10: 1}
    for k, v in dic.items():
        if price >= k:
            answer = int(price * v)
            return answer