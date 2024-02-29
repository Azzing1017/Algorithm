def solution(s):    
    li = []
    for x in s:
        if x == '(':
            li.append(x)
        else:
            try:
                li.pop()
            except IndexError:
                return False
    return not li