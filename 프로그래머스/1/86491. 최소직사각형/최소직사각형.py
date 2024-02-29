def solution(sizes):
    answer = 0
    
    x = 0
    y = 0
    for val in sizes:
        w, h = max(val[0], val[1]), min(val[0], val[1])
        x = max(x, w)
        y = max(y, h)        
    
    answer = x * y
    
    return answer