def solution(n, lost, reserve):
    answer = 0
    li = [1] * (n+2)
    for a in lost:
        li[a] = 0
    for b in reserve:
        li[b] += 1
    for i in range(1, n+1):
        if li[i] == 0:
            if li[i-1] == 2 or li[i+1] == 2:
                if li[i-1] != li[i+1]:
                    if li[i-1] == 2:
                        li[i-1] = 1
                    elif li[i+1] == 2:
                        li[i+1] = 1
                    li[i] = 1
    for i in range(1, n+1):
        if li[i] == 0:
            if li[i-1] == 2 or li[i+1] == 2:
                if li[i-1] == 2:
                    li[i-1] = 1
                elif li[i+1] == 2:
                    li[i+1] = 1
                li[i] = 1
    answer = n - li.count(0)
    return answer