from collections import deque

def solution(prices):
    
    prices_length = len(prices)
    answer = [0] * (prices_length)
    prices = prices
    
    for i in range(0, prices_length):
        cnt = 0
        for j in range(i + 1, prices_length):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer[i] = cnt
            
    return answer