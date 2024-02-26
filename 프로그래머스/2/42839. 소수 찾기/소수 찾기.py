def solution(numbers):
    answer = 0
    max_num = 9999999
    li = [True] * (max_num+1)
    li[0] = False
    li[1] = False
    for i in range(2, int(max_num**(1/2))+1):
        if li[i] == True:
            for j in range(i, max_num//i+1):
                li[i*j] = False
    ans = []
    len_numbers = len(numbers)
    tf = [False] * len_numbers
    def go(index, goal, word):
        if index == goal:
            ans.append(int(word))
            return
        else:
            for i in range(len_numbers):
                if tf[i] == False:
                    tf[i] = True
                    go(index+1, goal, word+numbers[i])
                    tf[i] = False
    for i in range(1, len_numbers+1):
        go(0, i, '')
        
    ans = set(ans)
    for i in ans:
        if li[i] == True:
            answer += 1
    
    return answer