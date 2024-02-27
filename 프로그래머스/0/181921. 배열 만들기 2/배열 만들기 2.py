def solution(l, r):
    answer = []
    def go(index, goal, tmp, li):
        if index == goal:
            if l <= int(tmp) <= r:
                answer.append(int(tmp))
        else:
            for a in li:
                go(index+1, goal, tmp+a, li)
    go(0, len(str(r)), '', ['0', '5'])
    if answer:
        answer = sorted(set(answer))
    else:
        answer = [-1]
    return answer