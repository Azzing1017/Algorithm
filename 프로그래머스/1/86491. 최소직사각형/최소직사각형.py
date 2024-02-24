def solution(sizes):
    answer = 0
    
    x = 0
    y = 0
    for val in sizes:
        w, h = val
        if h > w:
            w, h = h, w
        if w > x:
            x = w
        if h > y:
            y = h
    
    answer = x * y
    
    return answer